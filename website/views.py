from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

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

@permission_classes((IsAuthenticated, ))
class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer