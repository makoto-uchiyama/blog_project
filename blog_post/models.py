from pyexpat import model
from django.db import models

# Create your models here.
class SampleModel(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()

CATEGORY = (('buisiness','ビジネス'),('life','生活'),('other','その他'))
class BlogModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='タイトル')
    content = models.TextField(verbose_name='本文')
    postdate = models.DateField(auto_now_add=True, verbose_name='投稿日')
    category = models.CharField(max_length=50, choices=CATEGORY, verbose_name='カテゴリ')

    def __str__(self):
        return self.title