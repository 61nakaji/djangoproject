from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

GENDER_CHOICES = [
    ('1', '女性'),
    ('2', '男性'),
]

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Profile(models.Model):
    name = models.CharField('名前', max_length=100)
    gender = models.CharField('性別', max_length=1, choices=GENDER_CHOICES)
    yearly_income = models.IntegerField('年収(万円)')
    height = models.FloatField('身長')
    weight = models.FloatField('体重')
