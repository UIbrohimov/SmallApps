from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm
# Create your views here.

def list_view(request):
	post = Post.objects.all().order_by('-date')
	return render(request, 'post/post_list.html', {'post':post})

def detail_view(request, pk):
	post = Post.objects.get(pk=pk)
	# return HttpResponse('ishladi')
	return render(request, 'post/post_detail.html', {'post':post})

@login_required(login_url='/accounts/login/')
def create_view(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			# save files to the db
			# form.save()
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			return redirect('post:list_view')
	else:
		form = PostForm()
	return render(request, 'post/post_create.html', {'form':form})
