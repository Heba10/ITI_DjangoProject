from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ourBlog/',include('ourBlog.urls')),
    path('posts/',include('Posts.urls'))
]
