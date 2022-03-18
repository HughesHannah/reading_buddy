from django import forms
from django.contrib.auth.models import User
from readingBuddy.models import UserProfile
from readingBuddy.models import Comment, UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, help_text="We'd love for you to leave a comment.")

    class Meta:
        model = Comment
        fields = ('content',)