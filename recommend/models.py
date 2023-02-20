from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

MODE_CHOICES = [
    ('1', 'メジャー'),
    ('2', 'マイナー'),
]

class Profile(models.Model):
    name = models.CharField('曲名', max_length=100, null=True)
    album = models.CharField('アルバム名', max_length=100, null=True)
    artist = models.CharField('アーティスト名', max_length=100, null=True)
    length = models.IntegerField('曲の長さ', null=True)
    mode = models.CharField('曲調', max_length=1, choices=MODE_CHOICES, null=True)
    popularity = models.IntegerField('人気度', null=True)
    danceability = models.FloatField('ダンス度', null=True)
    acousticness = models.FloatField('アコースティック度', null=True)
