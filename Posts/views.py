from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post , Category ,Comments,Reply, Reaction, Subscribes,BadWord, Tags
import json
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


def addComment(request,postid): #the worst function i had done shitty code i know 
	if request.method=="POST":
		post= Post.objects.get(id=postid)
		uname = request.user # we have to replace it with auth user 
		con = request.POST.get('message')
		mptrn= r"^[\S][\S ]+$"
		result = re.match(mptrn, con)
		if (result):
			words =BadWord.objects.all()
			for word in words:
				rep=""
				size=len(word.word)
				for i in range(size):
					rep+="*"
				con = con.replace(word.word,rep)
			comm = Comments(post_name=post,user_name=uname,content=con)
			comm.save()
		
		return HttpResponseRedirect('/posts/'+postid )



def addReply(request,comid):
	if request.method =="POST":
		comment = Comments.objects.get(id = comid)
		uname = request.user
		con=request.POST.get('message')
		mptrn= r"^[\S][\S ]+$"
		result = re.match(mptrn, con)
		if(result):
			rep=Reply(user_name=uname,comment_name=comment,content=con)
			rep.save();
		return HttpResponseRedirect('/posts/'+str(comment.post_name_id))


def getSearchData(request):
	# if request.method =="GET":
	requiredSearch = request.GET['requiredSearch']
	# cat = Category.objects.get(name=requiredSearch)
	# post = Post.objects.filter(cat_name=cat)
	# tag = Tags.objects.filter(tag_name=requiredSearch)
	# return HttpResponse("heelllo")
	# if(requiredSearch=="none"):
	# 	return HttpResponseRedirect('/posts/')
	# else:
	tagPtrn=r"^#[\S]+$|^%23[\S]+$"
	titlePtrn=r"^[\S][\S ]+$"
	if(re.match(tagPtrn, requiredSearch)):
		try:
			tag=Tags.objects.get(tag_name=requiredSearch)
			posts=Post.objects.filter(tag_name=tag)
			context={'posts':posts}
		except Exception as e:
			context={'x':requiredSearch}
	elif(re.match(titlePtrn, requiredSearch)):
		posts=Post.objects.filter(title__contains=requiredSearch)
		context={'posts':posts}
	else:
		context={'x':requiredSearch}

	return render(request,'posts/index.html', context)
	# return HttpResponseRedirect('/posts/')


def listTags(request,tagid):
	tag=Tags.objects.get(id=tagid)
	posts=Post.objects.filter(tag_name=tag)
	cats = Category.objects.all()
	context={'posts':posts,'cats':cats}
	return render(request,'posts/index.html', context)