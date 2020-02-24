from django.shortcuts import render
from django.http import HttpResponse
from .models import Post , Category ,Comments,Reply, Reaction, Subscribes
import json

def homePage(request):
	posts = Post.objects.all().order_by('date')
	cats = Category.objects.all()
	context={'posts':posts,'cats':cats}
	return render(request,'posts/index.html', context)

def about(request):
	return render(request,'posts/about.html')

def displayPost(request,postid):
	post = Post.objects.get(id=postid)
	comments = Comments.objects.filter(post_name_id=postid)
	cats = Category.objects.all()
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


def getData(request):
	postId = request.GET['postId']
	userId = request.user
	reactState = request.GET['reactStatex']
	refresh = request.GET['refreshx']
	reaction, created = Reaction.objects.get_or_create(post_name_id=postId, user_name__username=userId)
	if(refresh=='0'):
		reaction.react=reactState
		reaction.save()
	else:
		pass
	likeReact = Reaction.objects.filter(react="like").count()
	dislikeReact = Reaction.objects.filter(react="dislike").count()


	return HttpResponse(json.dumps({'reactType':reaction.react, 'likeReact':likeReact, 'dislikeReact':dislikeReact}))

def getSubscribeData(request):
	userId = request.user
	catNum = request.GET['catNum']
	refresh = request.GET['refresh']
	# catState = request.GET['catState']

	cat=[]
	sub=[]
	if refresh=='1':
		subscribes = Subscribes
		for x in subscribes.objects.filter(user_name=userId):
			if x.user_name==userId:
				cat.append(x.cat_name.id)
			else:
				pass
	# subscribes, created = Subscribes.objects.get_or_create(user_name__username=userId, cat_name_id=catNum)
	else:
		subscribes, created = Subscribes.objects.get_or_create(user_name__username=userId, cat_name_id=catNum)
		if created==True:
			cat.append(subscribes.cat_name.id)
		else:
			subscribes.delete()

	return HttpResponse(json.dumps({'categoryNum':cat}))
