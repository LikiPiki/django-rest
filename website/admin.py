from django.contrib import admin
from .models import (
    Tag,
    Post
)


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    fields = ('name', )

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'content','likes')
    list_filter = ('title', 'content','likes', 'created_at') 
