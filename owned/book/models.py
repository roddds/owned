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
    target = models.PositiveIntegerField()

    required_items = models.ManyToManyField('book.Item', blank=True, related_name='enables_option')
    excluding_items = models.ManyToManyField('book.Item', blank=True, related_name='excludes_option')

    required_events = models.ManyToManyField('book.Event', blank=True, related_name='enables_option')
    excluding_events = models.ManyToManyField('book.Event', blank=True, related_name='excludes_option')

    paragraph = models.ForeignKey('book.Paragraph', related_name='options')

    def requirements_met(self, saveslot):
        logger.debug("checking requirements for option %d" % self.target)
        inventory = saveslot.inventory.all().values_list('id', flat=True)
        events = saveslot.events.all().values_list('id', flat=True)

        if self.required_items.exists():
            if not self.required_items.filter(id__in=inventory).exists():
                logger.debug("item requirements for option %d not met" % self.target)
                return False

        if self.excluding_items.exists():
            if self.excluding_items.filter(id__in=inventory).exists():
                logger.debug("item exclusion for option %d not met" % self.target)
                return False

        if self.required_events.exists():
            if not self.required_events.filter(id__in=events).exists():
                logger.debug("event requirements for option %d not met" % self.target)
                return False

        if self.excluding_events.exists():
            if self.excluding_events.filter(id__in=events).exists():
                logger.debug("event exclusion for option %d not met" % self.target)
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
