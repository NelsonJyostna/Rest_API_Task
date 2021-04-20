from django.db import models
from django.core import validators


# Create your models here.
class Song(models.Model):
      nameofSong=models.CharField(max_length=99)
      durinsec=models.PositiveIntegerField()
      uptime=models.DateTimeField(auto_now_add=False, auto_now=True)


class Podcast(models.Model):
       nameofPodcast=models.CharField(max_length=99)
       duration=models.PositiveIntegerField()
       uptime=models.DateTimeField(auto_now_add=False, auto_now=True)
       host=models.CharField(max_length=99)
       participants=models.CharField(null=True, max_length=99, validators=[validators.MaxLengthValidator(10)])


class AudioBook(models.Model):
      titleofAudio=models.CharField(max_length=99)
      authorofTitle=models.CharField(max_length=99)
      narator=models.CharField(max_length=99)
      duration=models.PositiveIntegerField()
      uptime=models.DateTimeField(auto_now_add=False,auto_now=True)




