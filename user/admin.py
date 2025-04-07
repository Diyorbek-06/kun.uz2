from django.contrib import admin
from .models import Comment,  User
# Register your models here.


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ('id', 'content', 'user', 'post')

admin.register(User)