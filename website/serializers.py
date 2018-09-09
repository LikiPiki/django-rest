from rest_framework import serializers
from .models import (
    Tag,
    Post
)

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class PostSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('title', 'content', 'likes', 'created_at', 'tags')
