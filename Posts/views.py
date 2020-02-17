from django.shortcuts import render
from django.http import HttpResponse
# from .models import Posts

def post_list(request):
	return HttpResponse("hello world")

