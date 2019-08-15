from django.db import models

# Create your models here.
#we need to install Pillow to use ImageField
#command is 'pip install Pillow'

class MovieModel(models.Model):
	title = models.CharField(max_length=120)
	description = models.CharField(max_length=120)
	rating = models.IntegerField()
	img = models.ImageField(upload_to = 'pics', default='null')