from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
    post = Post.objects.all().order_by('-date')
    return render(request, 'post/blog.html', {'post':post})