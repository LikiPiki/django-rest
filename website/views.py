from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import (
    Tag,
    Post
)
from .serializers import (
    TagSerializer,
    PostSerializer
)

def home_page(request):
    return HttpResponse("Hello page here")

# for django rest api
class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer