from .models import Comment, Post
from django.contrib import admin

# Register your models here.
class CommentInline(admin.StackedInline):
  model = Comment

class PostAdmin(admin.ModelAdmin):
  inlines = [CommentInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)