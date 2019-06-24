from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Video

class VideoListView(ListView):
	model = Video
	template_name = 'mainapp/home.html'
	context_object_name = 'videos'
	ordering = ['-date_posted']


class UploadVideo(CreateView):
	model = Video
	fields = ['title', 'description', 'thumbnail', 'video']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class VideoDetailView(DetailView):
	model = Video