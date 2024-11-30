from django import forms
from .models import Branch, Post, Comment


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['title', 'description']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
