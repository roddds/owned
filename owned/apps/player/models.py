from django.db import models
from book.models import Paragraph, Item, Event

import logging
logger = logging.getLogger("player")


class SaveSlot(models.Model):
    player_owner = models.ForeignKey('Player', related_name='save_slots')
    inventory = models.ManyToManyField('book.Item')
    events = models.ManyToManyField('book.Event')

    progress = models.ManyToManyField('book.Paragraph', through='player.Progress')

    is_started = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)

    current_chapter = models.SmallIntegerField(default=1)

    def set_as_active(self):
        self.player_owner.active_save_slot = self
        self.player_owner.save()
        logger.debug('Slot number %d set as active for player %s' % (self.index, self.player_owner.user.username))

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
            logger.debug(
'Added item "%s" to player %s\'s inventory' % (item.name,
                                              self.player_owner.user.username))

        for item in paragraph.removes_items.all():
            self.inventory.remove(item)
            logger.debug(
'Removed item "%s" from player %s\'s inventory' % (item.name,
                                                  self.player_owner.user.username))

        for event in paragraph.adds_events.all():
            self.events.add(event)
            logger.debug(
'Added event "%s" to player %s\'s events' % (event.label,
                                            self.player_owner.user.username))

        if paragraph.is_ending:
            self.is_finished = True
            logger.debug(
'Player %s reached an ending on chapter %s' % (self.player_owner.user.username,
                                              paragraph.id))

        p = Progress(paragraph=paragraph, save_slot=self)
        p.save()

    @property
    def index(self):
        return list(self.player_owner.save_slots.all()).index(self) + 1


    def __unicode__(self):
        return "SaveSlot %d for player %s" % (self.index, self.player_owner)

    class Meta:
        app_label = "player"


class Player(models.Model):
    user = models.OneToOneField('auth.User', related_name='player',
                                primary_key=True)
    endings = models.CharField(max_length=35,
                               default="0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
    is_active = models.BooleanField('Ativado', default=True)
    active_save_slot = models.ForeignKey('player.SaveSlot', blank=True, null=True)

    @staticmethod
    def setup(user):
        new_player = Player.objects.create(user=user)
        logger.debug("Player %s created" % new_player.user.username)
        save_slots = [SaveSlot.objects.create(player_owner=new_player) for x in range(3)]
        logger.debug("Created 3 save slots for player %s" % new_player.user.username)
        new_player.save()
        return new_player

    class Meta:
        app_label = "player"

    def __unicode__(self):
        return self.user.username


class Progress(models.Model):
    paragraph = models.ForeignKey('book.Paragraph')
    save_slot = models.ForeignKey('player.SaveSlot', related_name="progress_save_slot")
    time_played = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "player"
