from django.db import models
from book.models import Paragraph


class SaveSlot(models.Model):
    inventory = models.ManyToManyField('book.Item')
    events = models.ManyToManyField('book.Event')
    progress = models.ManyToManyField('book.Paragraph', through='Progress')

    class Meta:
        app_label = "player"


class Player(models.Model):
    user = models.OneToOneField('auth.User', related_name='player')
    active = models.BooleanField('Ativado', default=True)
    save_slot = models.ManyToManyField('player.SaveSlot', related_name="player_save_slot")

    class Meta:
        app_label = "player"


class Progress(models.Model):
    player = models.ForeignKey(Player)
    paragraph = models.ForeignKey(Paragraph)
    save_slot = models.ForeignKey(SaveSlot, related_name="progress_save_slot")

    class Meta:
        app_label = "player"
