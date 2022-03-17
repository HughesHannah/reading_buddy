from django import forms
from django.contrib.auth.models import User
from readingBuddy.models import UserProfile
from readingBuddy.models import Category, Book, Comment, UserProfile, ReadingList

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

