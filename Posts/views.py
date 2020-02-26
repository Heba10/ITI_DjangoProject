from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post , Category ,Comments,Reply, Reaction, Subscribes,BadWord, Tags
import json
import re
from .forms import postForm

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
			rels=[]
			reply = Reply.objects.filter(comment_name_id=comment.id)
			for r in reply :
				rels.append(r)
			dic = {'comm':comment , 'rep':rels[:]}
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
			words =BadWord.objects.all()
			for word in words:
				rep=""
				size=len(word.word)
				for i in range(size):
					rep+="*"
				con = con.replace(word.word,rep)
			rep=Reply(user_name=uname,comment_name=comment,content=con)
			rep.save();
		return HttpResponseRedirect('/posts/'+str(comment.post_name_id))


def getSearchData(request):
	if request.method =="GET":
		requiredSearch = request.GET['requiredSearch']
		cats = Category.objects.all()
		tagPtrn=r"^#[\S]+$"
		titlePtrn=r"^[\S][\S ]+$"
		if(re.match(tagPtrn, requiredSearch)):
			try:
				tag=Tags.objects.get(tag_name=requiredSearch)
				posts=Post.objects.filter(tag_name=tag)
				context={'posts':posts,'cats':cats}
			except Exception as e:
				context={'cats':cats}
		elif(re.match(titlePtrn, requiredSearch)):
			posts=Post.objects.filter(title__contains=requiredSearch)
			context={'posts':posts,'cats':cats}
		else:
			context={'cats':cats}

		return render(request,'posts/index.html', context)
	return HttpResponseRedirect('/posts/')


def listTags(request,tagid):
	tag=Tags.objects.get(id=tagid)
	posts=Post.objects.filter(tag_name=tag)
	cats = Category.objects.all()
	context={'posts':posts,'cats':cats}
	return render(request,'posts/index.html', context)

def addNewPost(request):
	new_post=None
	if request.method == 'POST':
		newPost = postForm(data=request.POST)
		if newPost.is_valid():
			new_post = newPost.save(commit=False)
			new_post.author = request.user
			new_post.save()
			return HttpResponseRedirect('/posts/')
	else:
		newPost = postForm()
	cats = Category.objects.all()
	context = {'newPost':newPost, 'cats':cats,'status':"new"}
	return render(request,'posts/newPost.html', context)


def editPost(request,postid):
	post = Post.objects.get(id=postid)
	if(request.user==post.author or request.user.is_staff):
		if request.method=="POST":
			form=postForm(request.POST,instance=post)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/posts/')
		else:
			form=postForm(instance=post)
			cats = Category.objects.all()
			context={'newPost':form, 'cats':cats,'status':"edit"}
			return render(request,'posts/newPost.html',context)
	else:
		return HttpResponseRedirect('/posts/')


def deletePost(request,postid):
	post = Post.objects.get(id=postid)
	if(request.user==post.author or request.user.is_staff):		
		post.delete()
	return HttpResponseRedirect('/posts/')


def listuser(request,userid):
	posts = Post.objects.filter(author_id=userid)
	cats = Category.objects.all()
	context={'posts':posts,'cats':cats}
	return render(request,'posts/index.html', context)



