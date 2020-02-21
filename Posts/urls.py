# from .models import Post
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	url(r'^$', views.homePage),
	url(r'^about$', views.about),
	# url(r'^(?P<slug>[\w-]+)/$', views.displayPost, name="postDetails"),
	path('<postid>', views.displayPost),
	path('listcat/<catid>', views.listCat),#i will try to fix it with url #osama
	# url(r'^listcat/{id}$', views.listCat),

]