from django.db import models
from book.models import Paragraph
from registration.signals import user_activated


class SaveSlot(models.Model):
    player_owner = models.ForeignKey('Player')
    inventory = models.ManyToManyField('book.Item')
    events = models.ManyToManyField('book.Event')
    progress = models.ManyToManyField('book.Paragraph', through='Progress')

    class Meta:
        app_label = "player"


class Player(models.Model):
    user = models.OneToOneField('auth.User', related_name='player', primary_key=True)
    endings = models.CharField(max_length=35, default="0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
    # active = models.BooleanField('Ativado', default=True)
    # save_slot = models.ManyToManyField('player.SaveSlot', related_name="player_save_slot")

    class Meta:
        app_label = "player"

    def __unicode__(self):
        return self.user.username


class Progress(models.Model):
    player = models.ForeignKey(Player)
    paragraph = models.ForeignKey(Paragraph)
    save_slot = models.ForeignKey(SaveSlot, related_name="progress_save_slot")

    class Meta:
        app_label = "player"


def make_player(sender, **kwargs):
    new_user = kwargs['user']
    # new_player, status = Player.objects.get_or_create(user=new_user)
    new_player = Player.objects.create(user=new_user)
    
user_activated.connect(make_player, dispatch_uid="player.models")