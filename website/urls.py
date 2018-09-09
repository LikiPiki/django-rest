from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'tags', views.TagsViewSet)
router.register(r'posts', views.PostViewset)

urlpatterns = [
    path('', views.home_page, name="home_page"),
    url(r'api/', include(router.urls)),
]
