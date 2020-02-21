from django.db import models
from django.contrib.auth.models import User
emotion = (('like','like'),('dislike','dislike'))


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


class Reaction(models.Model):
	user_name =models.CharField(max_length=25)
	post_name =models.ForeignKey(Post, on_delete=models.CASCADE)
	react =models.CharField(max_length=7,choices=emotion,default='like')

	def __str__(self):
		return '%s %s %s' % (self.post_name, self.user_name ,self.react)

class Subscribes(models.Model):
	user_name =models.CharField(max_length=25)
	cat_name =models.ForeignKey(Category, on_delete=models.DO_NOTHING)

	def __str__(self):
		return '%s %s' % (self.user_name, self.cat_name)

class Comments(models.Model):
	post_name = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
	user_name = models.CharField(max_length=25)
	content = models.CharField(max_length=200)
	date=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s %s' % (self.user_name, self.post_name)

class Reply(models.Model):
	user_name = models.CharField(max_length=25)
	comment_name = models.OneToOneField(Comments,on_delete=models.CASCADE)
	content = models.CharField(max_length=200)

	def __str__(self):
		return '%s %s' % (self.user_name, self.comment_name)

class Tags(models.Model):
	tag_name = models.CharField(max_length=15)
	post_name = models.ManyToManyField(Post,db_table="PostTags" )

	def __str__(self):
		return '%s %s' % (self.tag_name, self.post_name)


