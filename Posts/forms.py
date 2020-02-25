from django import forms
from .models import Comments, Post

class postForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'body', 'cat_name', 'thumbnail', 'tag_name')

# class commentForm(forms.ModelForm):
# 	class Meta:
# 		model = Comments
# 		fields = ('user_name','content')

		