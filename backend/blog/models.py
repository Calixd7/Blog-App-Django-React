from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify, title

class Categories(models.TextChoices):
    WORLD = 'world'
    ENVIROMENT = 'enviroment'
    DESIGN = 'design'
    TECHNOLOGY = 'technology'
    CULTURE = 'culture'
    POLITICS = 'politics'
    BUSINESS = 'business'
    OPINION = 'opinion'
    SCIENCE = 'science''
    HEALTH = 'health'
    STYLE = 'style'
    TRAVEL = 'travel'
class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    category = models.CharField(max_length=50, choices=Categories.choices, default=Categories.WORLD)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d')
    excerpt = models.CharField(max_length=150)
    month = models.CharField(max_length=3)
    day = models.CharField(max_length=2)
    content = models.TextField()