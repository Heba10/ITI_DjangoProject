from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post , Category

def post_list(request):
	posts = Post.objects.all().order_by('date')
	cats = Category.objects.all()
	context={'posts':posts,'cats':cats}
	return render(request,'posts/post_list.html', context)

