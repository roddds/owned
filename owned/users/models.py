# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
import uuid

from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from owned.book.models import Paragraph

import logging
logger = logging.getLogger("player")


@python_2_unicode_compatible
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    active_save_slot = models.ForeignKey('users.SaveSlot', blank=True, null=True)
    endings = models.CharField(max_length=35,
                               default="0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")

    def setup(self):
        logger.debug("Player %s created" % self.username)
        save_slots = [SaveSlot.objects.create(player_owner=self) for x in range(3)]
        logger.debug("Created 3 save slots for player %s" % self.username)
        self.save()
        return self


    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})


class SlotManager(models.Manager):
    def ordered(self):
        return self.all().order_by("id")

    def get_slot(self, index):
        return self.ordered()[index-1]


class SaveSlot(models.Model):
    objects = SlotManager()

    player_owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='save_slots')
    inventory = models.ManyToManyField('book.Item')
    events = models.ManyToManyField('book.Event')

    progress = models.ManyToManyField('book.Paragraph', through='users.Progress')

    is_started = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)

    current_chapter = models.SmallIntegerField(default=1)

    def set_as_active(self):
        self.player_owner.active_save_slot = self
        self.player_owner.save()
        logger.debug(
            'Slot number %d set as active for player %s' % (
                self.slot_number, self.player_owner.username))

    def new_game(self):
        self.set_as_active()
        self.current_chapter = 1
        self.is_started = True
        self.inventory.clear()
        self.events.clear()
        self.progress.clear()
        self.save()
        return self

    def add_item(self, item):
        self.inventory.add(item)

    def has_item(self, item):
        return self.inventory.filter(id=item.id).exists()

    def add_event(self, event):
        self.events.add(event)

    def has_event(self, event):
        return self.events.filter(id=event.id).exists()

    def play_chapter(self, chapter):
        self.current_chapter = chapter
        self.save()
        paragraph = Paragraph.objects.get(pk=chapter)
        if paragraph in self.progress.all():
            return

        for item in paragraph.adds_items.all():
            self.inventory.add(item)
            logger.info(
                'Added item "%s" to player %s\'s inventory' % (
                    item.name, self.player_owner.username))

        for item in paragraph.removes_items.all():
            self.inventory.remove(item)
            logger.info(
                'Removed item "%s" from player %s\'s inventory' % (
                    item.name, self.player_owner.username))

        for event in paragraph.adds_events.all():
            self.events.add(event)
            logger.info(
                'Added event "%s" to player %s\'s events' % (
                    event.label, self.player_owner.username))

        if paragraph.is_ending:
            self.is_finished = True
            logger.info(
                'Player %s reached an ending on chapter %s' % (
                    self.player_owner.username, paragraph.id))

        p = Progress(paragraph=paragraph, save_slot=self)
        p.save()

    @property
    def slot_number(self):
        number = list(self.player_owner.save_slots.ordered()).index(self) + 1
        logger.debug("%s identified as number %s" % (self.id, number))
        return number

    def __unicode__(self):
        return "SaveSlot %d for player %s" % (self.slot_number, self.player_owner)


class Progress(models.Model):
    paragraph = models.ForeignKey('book.Paragraph')
    save_slot = models.ForeignKey('users.SaveSlot', related_name="progress_save_slot")
    time_played = models.DateTimeField(auto_now_add=True)
