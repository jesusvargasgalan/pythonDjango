from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
  auhor = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  slug = models.CharField(max_length=300)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(null=True, blank=True) 

  def __str__(self):
    return f'Post {self.title} {self.id}'

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def is_published(self) -> bool:
    return self.published_date is not None