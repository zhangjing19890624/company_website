from idlelib.pyshell import usage_msg

from django.db import models

# Create your models here.

class NewsType(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "新闻分类"
        verbose_name_plural = "新闻分类"

class News(models.Model):
    type = models.ForeignKey(NewsType, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    order = models.IntegerField(default=0)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title

    class Meta:
        verbose_name = "新闻"
        verbose_name_plural = "新闻"