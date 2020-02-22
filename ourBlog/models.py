from django.db import models

# Create your models here.
from django.contrib.auth.models import User

emotion = (('like', 'like'), ('dislike', 'dislike'))


class Category(models.Model):
    pass

class Post(models.Model):
    pass