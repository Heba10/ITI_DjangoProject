from django.shortcuts import render
from django.http import HttpResponse
from .models import Post , Category

def homePage(request):
	posts = Post.objects.all().order_by('date')
	cats = Category.objects.all()
	context={'posts':posts,'cats':cats}
	return render(request,'posts/index.html', context)

def about(request):
	return render(request,'posts/about.html')

def displayPost(request,slug):
	post = Post.objects.get(slug=slug)
	# return HttpResponse(slug)
	return render(request, 'posts/single.html', {'post':post})

def listCat(request,catid):
	posts = Post.objects.filter(cat_name_id=catid)
	cats = Category.objects.all()
	context={'posts':posts,'cats':cats}
	return render(request,'posts/post_list.html', context)
