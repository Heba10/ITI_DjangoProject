# from .models import Post
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	url(r'^$', views.post_list),
	path('listcat/<catid>', views.listCat),#i will try to fix it with url #osama
	# url(r'^listcat/{id}$', views.listCat),

]