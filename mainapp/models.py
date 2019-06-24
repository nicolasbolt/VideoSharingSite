from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Video(models.Model):
	#Set up video fields in the database
	title = models.CharField(max_length=100)
	description = models.TextField(null=True)
	video = models.FileField(blank="True", null="True", upload_to="videos/")
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	thumbnail = models.ImageField(default="default-thumbnail.jpg", upload_to="thumbnails/")

	def __str__(self):
		return self.title + ": " + str(self.video)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.thumbnail.path)

		if img.height > 300 or img.width > 300:
			output_size = (426, 240)
			img.thumbnail(output_size)
			img.save(self.thumbnail.path)

	def get_absolute_url(self):
		return reverse('home')