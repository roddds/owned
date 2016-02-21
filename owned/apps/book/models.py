from django.db import models

import logging
logger = logging.getLogger(__name__)


class Event(models.Model):
    label = models.TextField()

    class Meta:
        app_label = 'book'

    def __unicode__(self):
        return '%s: %s' % (self.pk, self.label)


class Item(models.Model):
    name = models.TextField()
    description = models.TextField(null=True, blank=True)
    image_filename = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = "book"


class Option(models.Model):
    text = models.TextField()
    target = models.PositiveIntegerField(null=True)

    required_items = models.ManyToManyField('book.Item', blank=True, related_name='item_required_in')
    excluding_items = models.ManyToManyField('book.Item', blank=True, related_name='item_excluding_in')

    required_events = models.ManyToManyField('book.Event', blank=True, related_name='event_required_in')
    excluding_events = models.ManyToManyField('book.Event', blank=True, related_name='event_excluding_in')

    paragraph = models.ForeignKey('Paragraph', null=True)

    def requirements_met(self, saveslot):
        logger.debug("checking requirements for option %d" % self.target)

        if not all (self.required_items.exists(),
                    self.required_events.exists(),
                    self.excluding_items.exists(),
                    self.excluding_events.exists()):
            logger.debug("option %d has no requirements" % self.target)
            return True

        logger.debug("getting player's inventory and events")
        inventory = saveslot.inventory.all()
        events = saveslot.events.all()

        logger.debug("checking requirements")
        required_items = self.required_items.all()
        logger.debug("option %d has %d required items" % (self.target, required_items.count()))
        required_events = self.required_events.all()
        logger.debug("option %d has %d required events" % (self.target, required_events.count()))

        excluding_items = self.excluding_items.all()
        logger.debug("option %d has %d excluding items" % (self.target, excluding_items.count()))
        excluding_events = self.excluding_events.all()
        logger.debug("option %d has %d excluding events" % (self.target, excluding_events.count()))

        for item in required_items:
            if item not in inventory:
                logger.debug("%d DISABLED: item %s not in inventory" % (self.target, item.name))
                return False

        for event in required_events:
            if event not in events:
                logger.debug("%d DISABLED: event %s not in events" % (self.target, event.label))
                return False

        for item in excluding_items:
            if item in inventory:
                logger.debug("%d DISABLED: excluding item %s in inventory" % (self.target, item.name))
                return False

        for event in excluding_events:
            if event in events:
                logger.debug("%d DISABLED: excluding event %s in events" % (self.target, event.label))
                return False

        return True


    class Meta:
        app_label = 'book'

    def __unicode__(self):
        return '%s: %s' % (self.target, self.text)


class Paragraph(models.Model):
    title = models.TextField()
    text = models.TextField()
    adds_items = models.ManyToManyField('book.Item', related_name='adds_items', blank=True)
    removes_items = models.ManyToManyField('book.Item', related_name='removes_items', blank=True)
    adds_events = models.ManyToManyField('book.Event', related_name='adds_events', blank=True)
    is_ending = models.BooleanField(default=False)

    def display_text(self):
        return self.text
    display_text.allow_tags = True

    class Meta:
        app_label = 'book'

    def __unicode__(self):
        return '%s: %s' % (self.title, " ".join(self.text.split()[:5])+'...')
