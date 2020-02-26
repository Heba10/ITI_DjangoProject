from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from Posts.models import Post,Category,Reply,Comments

# Create your views here.

def users(request):
    users = User.objects.all()
    u = User.get_username
    mainContentVar = "Users"
    context = {'u':u,'users':users,'mainContentVar': mainContentVar}
    return render(request,'admin/content/usersTable.html',context)

def categories(request):
    cat = Category.objects.all()
    mainContentVar = "Categories"
    context = {'cat':cat,'mainContentVar':mainContentVar}
    return render(request,'admin/content/categories.html',context)

def posts(request):
    post = Post.objects.all()
    mainContentVar = "Posts"
    context = {'post':post,'mainContentVar':mainContentVar}
    return render(request,'admin/content/postsList.html',context)

def editPost(request,num):
    pass

def deletePost(request,post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect("/ourBlog/posts")


def words(request):
    mainContentVar = "Forbidden Words"
    context = {'mainContentVar': mainContentVar}
    return render(request,'admin/content/wordsForbidden.html',context)

