from django.shortcuts import get_object_or_404, render
from .models import Post

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
