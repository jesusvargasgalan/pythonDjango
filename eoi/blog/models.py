from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
  auhor = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(null=True, blank=True) 

  def __str__(self):
    return f'Post {self.title} {self.id}'