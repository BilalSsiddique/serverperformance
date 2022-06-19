from .models import *
from django import forms
from django.contrib.auth.models import User
# from .models import user
from django.contrib.auth.forms import UserCreationForm


class userform(UserCreationForm):
    class Meta:
        model = user
        fields = ['email', 'name', 'password1',
                  'roleid', 'is_active', 'is_staff']
