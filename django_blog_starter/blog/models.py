from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=300)
  pub_date = models.DateField('date published')
  content = models.TextField()

  def __str__(self):
      return self.title


class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  content = models.TextField
  pub_date = models.DateTimeField('date published')
  author = models.CharField(max_length = 100)
