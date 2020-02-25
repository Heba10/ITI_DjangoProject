# from .models import Post
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	url(r'^$', views.homePage),
	url(r'^about$', views.about),
	url(r'^(?P<postid>[\w])/$', views.displayPost),
	path('listcat/<catid>', views.listCat),#i will try to fix it with url #osama
    url(r'^like$', views.getData),
    url(r'^subscribe$', views.getSubscribeData),
    path('<postid>/addcomment',views.addComment),
    path('<comid>/addreply',views.addReply),
    url(r'^searchResult$', views.getSearchData),
    path('listtag/<tagid>',views.listTags),
    url('newPost',views.addNewPost),
    path('editpost/<postid>',views.editPost),

	# url(r'^(?P<slug>[\w-]+)/$', views.displayPost, name="postDetails"),
	# url(r'^listcat/{id}$', views.listCat),
	# url(r'^like/(?P<postId>[\w]+)/(?P<userId>[\w]+)/(?P<reactState>[\w]+)/(?P<refresh>[\w]+)$', views.getData),
    
]