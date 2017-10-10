from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)

class CommentAdmin(admin.ModelAdmin):
	"""docstring for CommentAdmin"""
	list_display = ('user', 'email', 'approved')

admin.site.register(Comment, CommentAdmin)