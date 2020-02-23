from django import forms
from .models import Comments


class commentForm(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ('user_name','content')

		