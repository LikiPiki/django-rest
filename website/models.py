from django.db import models

# Create your models here.

class Tag(models.Model):
    """Tag simple model"""
    created_at = models.DateTimeField("Created date", auto_now_add=True)
    name = models.TextField("Name", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = 'Тэги'
    

class Post(models.Model):
    """Simple blog post model"""
    title = models.TextField("Title", max_length=100)
    content = models.TextField("Content", max_length=4000)
    likes = models.PositiveIntegerField("Likes", default=0)
    tags = models.ManyToManyField(Tag)

    created_at = models.DateTimeField("Created date", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог пост"
        verbose_name_plural = 'Блог посты'
