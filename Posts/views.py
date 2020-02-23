from django.shortcuts import render
from django.http import HttpResponse
from .models import Post , Category ,Comments,Reply, Reaction
import re

def homePage(request):
	posts = Post.objects.all().order_by('date')
	cats = Category.objects.all()
	context={'posts':posts,'cats':cats}
	return render(request,'posts/index.html', context)

def about(request):
	return render(request,'posts/about.html')

def displayPost(request,postid):#osama will rewrite this function to be simple
	post = Post.objects.get(id=postid)
	cats = Category.objects.all()
	comments = Comments.objects.filter(post_name_id=postid)
	data = []
	for comment in comments :
		try:
			reply = Reply.objects.get(comment_name_id=comment.id)
			dic = {'comm':comment , 'rep':reply}
		except Exception as e:
			dic={'comm':comment }
		finally:
			data.append(dic)

	context={'post':post,'data':data,'cats':cats}
	return render(request, 'posts/single.html',context)

def listCat(request,catid):
	posts = Post.objects.filter(cat_name_id=catid)
	cats = Category.objects.all()
	context={'posts':posts,'cats':cats}
	return render(request,'posts/index.html', context)


def getData(request, postId, userId, reactState, refresh):
	# postId = request.GET['postId']
	# userId = request.GET['userId']
	# reactState = request.GET['reactStatex']
	# refresh = request.GET['refreshx']
	reaction, created = Reaction.objects.get_or_create(post_name_id=postId, user_name__username=userId)
	if(refresh=='0'):
		reaction.react=reactState
		reaction.save()
	else:
		pass
	# reaction.save()
	# reaction = Reaction.objects.get(post_name_id=postId, user_name__username=userId)
	return HttpResponse( reaction.react)
	# return HttpResponse('hello'+postId+'hello')


def addComment(request,postid): #the worst function i had done shitty code i know 
	if request.method=="POST":
		post= Post.objects.get(id=postid)
		uname = request.user # we have to replace it with auth user 
		con = request.POST.get('message')
		mptrn= r"^[\S][\S ]+$"
		result = re.match(mptrn, con)
		if (result):
			comm = Comments(post_name=post,user_name=uname,content=con)
			comm.save()
		#i want call function display post here but i cant i will try later #osama
		post = Post.objects.get(id=postid)
		cats = Category.objects.all()
		comments = Comments.objects.filter(post_name_id=postid)
		data = []
		for comment in comments :
			try:
				reply = Reply.objects.get(comment_name_id=comment.id)
				dic = {'comm':comment , 'rep':reply}
			except Exception as e:
				dic={'comm':comment }
			finally:
				data.append(dic)

		context={'post':post,'data':data,'cats':cats}
		return render(request, 'posts/single.html',context)
