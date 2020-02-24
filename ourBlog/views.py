from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from Posts.models import Post, Category, Reply, Comments


# Create your views here.

def users(request):
    users = User.objects.all()
    u = User.get_username
    mainContentVar = "Users"
    context = {'u': u, 'users': users, 'mainContentVar': mainContentVar}
    return render(request, 'admin/content/usersTable.html', context)


def categories(request):
    cat = Category.objects.all()
    mainContentVar = "Categories"
    context = {'cat': cat, 'mainContentVar': mainContentVar}
    return render(request, 'admin/content/categories.html', context)


def posts(request):
    post = Post.objects.all()
    mainContentVar = "Posts"
    context = {'post': post, 'mainContentVar': mainContentVar}
    return render(request, 'admin/content/postsList.html', context)


def editPost(request, num):
    pass


def deletePost(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect("/ourBlog/posts")


def words(request):
    mainContentVar = "Forbidden Words"
    context = {'mainContentVar': mainContentVar}
    return render(request, 'admin/content/wordsForbidden.html', context)


# user -> admin
def grantUser(request, username):
    user = User.objects.get(username=username)
    user.is_staff = True
    user.is_admin = True
    user.is_superuser = True
    user.save()
    return HttpResponseRedirect("/ourBlog/users")


# admin -> user
def revokeUser(request, username):
    user = User.objects.get(username=username)
    user.is_staff = False
    user.is_admin = False
    user.is_superuser = False
    user.save()
    return HttpResponseRedirect("/ourBlog/users")


# user can't login
def blockUser(request, username):
    pass


def unblockUser(request, username):
    pass


def delUser(request,username):
    try:
        user = User.objects.get(username=username)
        user.delete()
        return HttpResponseRedirect("/ourBlog/users")

    except User.DoesNotExist:
        return HttpResponseRedirect("/ourBlog/users")

