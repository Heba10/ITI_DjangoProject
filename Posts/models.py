from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name
		
class Post(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	cat_name =models.ForeignKey(Category, on_delete=models.DO_NOTHING)
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
	thumbnail = models.ImageField(default='default.png', blank=True)
	def __str__(self):
		return self.title

	def abstractBody(self):
		return self.body[:150]+'...'

