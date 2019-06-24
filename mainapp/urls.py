from django.contrib import admin
from django.urls import path
from .views import VideoListView, UploadVideo, VideoDetailView

urlpatterns = [
    path('', VideoListView.as_view(), name='home'),
    path('video/new/', UploadVideo.as_view(), name='video-upload'),
    path('video/<int:pk>/', VideoDetailView.as_view(), name='video-detail'),
]
