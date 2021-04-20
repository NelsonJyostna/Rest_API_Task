from django.shortcuts import render
from rest_framework.response import Response
from .models import Song, Podcast, AudioBook
from .serializers import SongSerializer, PodcastSerializer, AudioBookSerializer
from rest_framework import status
from rest_framework.views import APIView


# Song API
class SongAPI(APIView):
       def get(self, request, pk=None):
           id=pk
           if id is not None:
              song=Song.objects.get(id=id)
              serializer=SongSerializer(song)
              return Response(serializer.data)
           else:
               songs=Song.objects.all()
               serializer=SongSerializer(songs, many=True)
               return Response(serializer.data, status=status.HTTP_200_OK)

       def post(self, request):
           serializer=SongSerializer(data=request.data)
           if serializer.is_valid():
               serializer.save()
               return Response({'msg': "Song Added"})
           else:
               return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

       def put(self, request, pk):
           id=pk
           song=Song.objects.get(pk=id)
           serializer=SongSerializer(song, request.data)
           if serializer.is_valid():
               serializer.save()
               return Response({'msg': 'Song Updated'})
           else:
               return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

       def delete(self, request, pk):
           id=pk
           song=Song.objects.get(id=pk)
           song.delete()
           return Response({'msg':'Data Deleted'})


#Podcast_API
class PodcastAPI(APIView):
       def get(self, request, pk=None):
            id = pk
            if id is not None:
               pod = Podcast.objects.get(id=id)
               serializer = PodcastSerializer(pod)
               return Response(serializer.data)
            else:
               pods = Podcast.objects.all()
               serializer = PodcastSerializer(pods, many=True)
               return Response(serializer.data, status=status.HTTP_200_OK)

       def post(self, request):
            serializer = PodcastSerializer(data=request.data)
            if serializer.is_valid():
               serializer.save()
               return Response({'msg': "Podcast Added"})
            else:
               return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

       def put(self, request, pk):
            id = pk
            pod = Podcast.objects.get(pk=id)
            serializer = PodcastSerializer(pod, request.data)
            if serializer.is_valid():
               serializer.save()
               return Response({'msg': 'Podcast Updated'})
            else:
               return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

       def delete(self, request, pk):
            id = pk
            pod = Podcast.objects.get(id=pk)
            pod.delete()
            return Response({'msg': 'Podcast Data Deleted'})


#AudioBook_API
class AudioBookAPI(APIView):
       def get(self, request, pk=None):
            id = pk
            if id is not None:
               audio = AudioBook.objects.get(id=id)
               serializer = AudioBookSerializer(audio)
               return Response(serializer.data)
            else:
              audios = AudioBook.objects.all()
              serializer = AudioBookSerializer(audios, many=True)
              return Response(serializer.data, status=status.HTTP_200_OK)

       def post(self, request):
           serializer = AudioBookSerializer(data=request.data)
           if serializer.is_valid():
              serializer.save()
              return Response({'msg': "AudioBook Added"})
           else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

       def put(self, request, pk):
           id = pk
           audio = AudioBook.objects.get(pk=id)
           serializer = AudioBookSerializer(audio, request.data)
           if serializer.is_valid():
              serializer.save()
              return Response({'msg': 'AudioBook Updated'})
           else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

       def delete(self, request, pk):
           id = pk
           audio = AudioBook.objects.get(id=pk)
           audio.delete()
           return Response({'msg': 'AudioBook Data Deleted'})