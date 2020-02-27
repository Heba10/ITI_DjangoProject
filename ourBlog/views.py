from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from Posts.models import Post, Category, BadWord
from .forms import createUserForm, createCategoryForm, createBadWordForm,changePassForm


# Create your views here.

def adminHome(request):
    return render(request, 'admin/content/adminHome.html')


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


def deletePost(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect("/ourBlog/posts")


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
    user = User.objects.get(username=username)
    user.is_active = False
    user.save()
    return HttpResponseRedirect("/ourBlog/users")


def unblockUser(request, username):
    user = User.objects.get(username=username)
    user.is_active = True
    user.save()
    return HttpResponseRedirect("/ourBlog/users")


def delUser(request, username):
    try:
        user = User.objects.get(username=username)
        user.delete()
        return HttpResponseRedirect("/ourBlog/users")

    except User.DoesNotExist:
        return HttpResponseRedirect("/ourBlog/users")


def createUser(request):
    if request.method == "POST":
        user_form = createUserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect("/ourBlog/users")
    else:
        user_form = createUserForm()
        context = {'user_form': user_form}
        return render(request, 'admin/content/createUser.html', context)


def editUser(request, username):
    user = User.objects.get(username=username)
    context = {'user': user}
    if user.is_staff:
        return render(request, 'ourBlog/posts', context)
    else:
        return render(request, 'admin/content/editUser.html', context)


def saveState(request, id, *args):
    if request.POST.get('cancel'):
        return HttpResponseRedirect("/ourBlog/users")
    else:
        user = User.objects.get(id=id)
        fname = request.POST.get('fname')
        user.first_name = fname
        lname = request.POST.get('lname')
        user.last_name = lname
        email = request.POST.get('email')
        user.email = email
        username = request.POST.get('username')
        user.username = username
        user.save()
        return HttpResponseRedirect("/ourBlog/users")


def addCat(request):
    if request.method == "POST":
        category_form = createCategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect("/ourBlog/categories")
    else:
        category_form = createCategoryForm()
        context = {'category_form': category_form}
        return render(request, 'admin/content/createCategory.html', context)


def editCat(request, id):
    cat = Category.objects.get(id=id)
    if request.method == "POST":
        category_form = createCategoryForm(request.POST, instance=cat)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect("/ourBlog/categories")
    else:
        category_form = createCategoryForm(instance=cat)
        context = {'category_form': category_form}
        return render(request, 'admin/content/createCategory.html', context)


def deleteCat(request, id):
    cat = Category.objects.get(id=id)
    cat.delete()
    return HttpResponseRedirect("/ourBlog/categories")


def words(request):
    word = BadWord.objects.all()
    mainContentVar = "Forbidden Words"
    context = {'word': word, 'mainContentVar': mainContentVar}
    return render(request, 'admin/content/wordsForbidden.html', context)


def deleteWord(request, id):
    word = BadWord.objects.get(id=id)
    word.delete()
    return HttpResponseRedirect("/ourBlog/words")


def addWord(request):
    if request.method == "POST":
        badWord_form = createBadWordForm(request.POST)
        if badWord_form.is_valid():
            badWord_form.save()
            return HttpResponseRedirect("/ourBlog/words")
    else:
        badWord_form = createBadWordForm()
        context = {'badWord_form': badWord_form}
        return render(request, 'admin/content/createBadWord.html', context)


def editWord(request, id):
    word = BadWord.objects.get(id=id)
    if request.method == "POST":
        badWord_form = createBadWordForm(request.POST, instance=word)
        if badWord_form.is_valid():
            badWord_form.save()
            return HttpResponseRedirect("/ourBlog/words")
    else:
        badWord_form = createBadWordForm(instance=word)
        context = {'badWord_form': badWord_form}
        return render(request, 'admin/content/createBadWord.html', context)


def changePass(request,username):
    user = User.objects.get(username=username)
    if request.method == "POST":
        changePass_form = changePassForm(request.POST, instance=user)
        if changePass_form.is_valid():
            changePass_form.save()
            user.save()
            return HttpResponseRedirect("/ourBlog/users")
    else:
        changePass_form = changePassForm(instance=user)
        context = {'changePass_form': changePass_form}
        return render(request, 'admin/content/changePass.html', context)

