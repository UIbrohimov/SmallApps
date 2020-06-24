from django.shortcuts import render
from django.http import HttpResponse
from post.models import Article
# Create your views here.

def list_view(request):
    articles = Article.objects.all().order_by('-date')
    return render(request, 'post/post_list.html', {'articles':articles})

def about_view(request):
    return render(request, 'post/about.html')

def detail_view(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'post/post_detail.html', {'article':article})
