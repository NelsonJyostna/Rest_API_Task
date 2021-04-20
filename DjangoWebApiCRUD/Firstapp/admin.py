from django.contrib import admin
from .models import *


# Register your models here.

class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'nameofSong', 'durinsec', 'uptime']
admin.site.register(Song, SongAdmin)



class PodcastAdmin(admin.ModelAdmin):
    list_display = ['id', 'nameofPodcast', 'duration', 'uptime', 'host', 'participants']
admin.site.register(Podcast, PodcastAdmin)



class AudioBookAdmin(admin.ModelAdmin):
      list_display = ['id', 'titleofAudio', 'authorofTitle', 'narator', 'duration', 'uptime']
admin.site.register(AudioBook, AudioBookAdmin )

