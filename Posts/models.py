from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	#author
	#thumbnail
	def __str__(self):
		return self.title

	def abstractBody(self):
		return self.body[:150]+'...'