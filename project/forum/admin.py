from django.contrib import admin
from .models import Branch, Post, Comment


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['branch', 'author', 'title', 'views', 'created_at']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'created_at']
