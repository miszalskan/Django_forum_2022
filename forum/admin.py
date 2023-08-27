from django.contrib import admin
from .models import Post, Comment
from django.contrib.auth.models import User


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'body', 'created_on')
    list_filter = ['created_on']
    search_fields = ['name', 'body']


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_on')
    search_fields = ['title', 'content']


class UserAdmin(admin.ModelAdmin):
    model = User
    email = User.email
    fields = ['username', 'email']


admin.site.register(Post, PostAdmin)
admin.site.unregister(User)
admin.site.register(User)
admin.site.register(Comment, CommentAdmin)
