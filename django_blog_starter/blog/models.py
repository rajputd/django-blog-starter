from django.db import models
from django.utils import timezone

snippet_length = 200

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=300)
  pub_date = models.DateField('date published', default=timezone.now)
  content = models.TextField()

  def getSnippet(self):
    if len(self.content) < snippet_length:
      return self.content
    else:
      return self.content[0:snippet_length - 3] + "..."

  def __str__(self):
      return self.title


class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  content = models.TextField(default="")
  pub_date = models.DateTimeField('date published', default=timezone.now)
  author = models.CharField(max_length = 100)

  def __str__(self):
    return self.author + " | " + str(self.pub_date)
