from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Comment, Post

# Create your views here.
def index(request):
  all_posts = Post.objects.all()
  context = {
    'posts': all_posts
  }
  return render(request, 'blog/index.html', context)

def post(request, post_id):
  post = get_object_or_404(Post, pk=post_id)
  return render(request, 'blog/post.html', {'post' : post})

def submit_comment(request, post_id):
  post = get_object_or_404(Post, pk=post_id)
  try:
    comment_content = request.POST['content']
    comment_author = request.POST['author']
  except (KeyError) as e:
    return render(request, 'blog/post.html', {
      'post' : post,
      'error_message': 'Please fill out the comment form completely'
    })
  else:
    post.comment_set.create(
      content = comment_content,
      author=comment_author,
      pub_date=timezone.now()
    )
    return render(request, 'blog/post.html', {
      'post' : post,
    })

