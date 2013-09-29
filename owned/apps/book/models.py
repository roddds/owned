from django.db import models


class Event(models.Model):
    label = models.TextField()

    class Meta:
        app_label = 'book'

    def __unicode__(self):
        return '%s: %s' % (self.pk, self.label)


class Item(models.Model):
    name = models.TextField()
    item_id = models.IntegerField(null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="images")

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = "book"


class Option(models.Model):
    text = models.TextField()
    target = models.PositiveIntegerField(null=True)
    item_requirements = models.ManyToManyField('book.Item', blank=True)
    event_requirements = models.ManyToManyField('book.Event', blank=True)

    paragraph = models.ForeignKey('Paragraph', null=True)

    def requirements_met(self, saveslot):
        inventory = saveslot.inventory.all()
        events = saveslot.events.all()

        for item in self.item_requirements.all():
            if item not in inventory:
                return False

        for item in self.item_requirements.all():
            if item not in inventory:
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
