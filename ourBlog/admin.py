from django.contrib import admin

# Register your models here.
from django.shortcuts import render

from django.utils.html import format_html
from .models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_per_page = 10
    list_max_show_all = 50


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "added_by", "action_btn")
    search_fields = ("title", "category__name")
    actions = None
    list_display_links = ("category", "added_by")
    change_list_template = "admin/posts/list.html"
    change_form_template = "admin/posts/edit.html"
    list_per_page = 10
    list_max_show_all = 50

    def action_btn(self, obj):
        html = '<a class="btn btn-default" href="/admin/ourBlog/post' + str(obj.id) + '/change/">Edit</a>'
        html = '<a class="btn btn-default" href="/admin/ourBlog/post' + str(obj.id) + '/delete/">Delete</a>'

        return format_html(html)

    action_btn.short_description = "Action"

    def get_view_data(self, request, object_id):
        try:
            object_id = 4
            data = Post.object.get(id.object_id)
            return render("admin/blog/view.html")
        except:
            return render("admin/blog/nodata.html")
