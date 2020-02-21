from django.contrib import admin
from .models import Post,Category,Reaction,Subscribes,Comments,Reply,Tags

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Reaction)
admin.site.register(Subscribes)
admin.site.register(Comments)
admin.site.register(Reply)
admin.site.register(Tags)
