from django.urls import path
from . import views

urlpatterns = [
    path('song/', views.SongAPI.as_view() ),
    path('song/<int:pk>/', views.SongAPI.as_view() ),

    path('podcast/', views.PodcastAPI.as_view()),
    path('podcast/<int:pk>/', views.PodcastAPI.as_view()),


    path('audio/', views.AudioBookAPI.as_view()),
    path('audio/<int:pk>/', views.AudioBookAPI.as_view()),

]