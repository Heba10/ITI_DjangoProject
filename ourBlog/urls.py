"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from ourBlog import views

urlpatterns = [
    path('admin/', views.adminHome),
    path('posts/', views.posts),
    path('newPost/', views.createUser),
    path('delPost/<post_id>', views.deletePost),
    path('users/', views.users),
    path('changePass/<username>', views.changePass),
    path('users/revoke/<username>', views.revokeUser),
    path('users/grant/<username>', views.grantUser),
    path('users/block/<username>', views.blockUser),
    path('users/unblock/<username>', views.unblockUser),
    path('users/delete/<username>', views.delUser),
    path('users/editUser/<username>', views.editUser),
    path('users/saveState/<id>', views.saveState),
    path('users/createUser/', views.createUser),
    path('categories/', views.categories),
    path('categories/editCat/<id>', views.editCat),
    path('categories/deleteCat/<id>', views.deleteCat),
    path('categories/addCat/', views.addCat),
    path('words/', views.words),
    path('words/editWord/<id>', views.editWord),
    path('words/deleteWord/<id>', views.deleteWord),
    path('words/addWord/', views.addWord),
]
