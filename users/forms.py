from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AuthFormCheckStatus(AuthenticationForm):
    error_messages = {
        'invalid_login': (
            "Please enter a correct username and password . Note that both "
            "fields may be case-sensitive ."
        ),
        'inactive': ("This account is block.you should contact the admin "),

    }

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.User_cache = authenticate(self.request, username=username, password=password)
            if self.User_cache is None:
                try:
                    user_temp = User.objects.get(username=username)
                except:
                    user_temp = None

                if user_temp is not None:
                    self.confirm_login_allowed(user_temp)

                raise self.get_invalid_login_error()
        return self.cleaned_data
