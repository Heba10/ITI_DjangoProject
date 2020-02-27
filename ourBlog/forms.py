from django import forms
from django.contrib.auth.models import User
from Posts.models import Category,BadWord


class createUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class createCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class createBadWordForm(forms.ModelForm):
    class Meta:
        model = BadWord
        fields = ('word',)
        widgets = {
            'word': forms.TextInput(attrs={'class': 'form-control'}),
        }

class changePassForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'password'}
        widgets = {
            'password': forms.TextInput(attrs={'class': 'form-control'}),
        }