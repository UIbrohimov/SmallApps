from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Photo, Poem, Post, Comment
from .forms import EmailPostForm
from django.views import generic    
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# importing forms
from .forms import CommentForm #EmailPostForm
from django.core.mail import send_mail
# importing Q for search engine
from django.db.models import Q
# Create your views here.


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 8
    template_name = 'poems/blog.html'
  
class SearchResultView(ListView):
    model = Post
    template_name = 'poems/search_result.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
        return object_list

# def post_list(request):
#     object_list = Post.published.all()
#     paginator = Paginator(object_list, 3) # 3 posts in each page
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer deliver the first page
#         posts = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range deliver last page of results
#         posts = paginator.page(paginator.num_pages)
        # return render(request,'poems/post_list.html',{'page': page,'posts': posts})


def post_share(request, id):

    # return render(request, 'poems/send.html')
    # return HttpResponse('form was submitted!')
    # Retrieve post by id
    post = get_object_or_404(Post, id=id, status='published')
    sent = False
    if request.method == 'POST':
        # Form was submitted
       
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # return HttpResponse('Form fields passed validation')
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments:{}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'ubuhobbit@gmail.com',[cd['to']], fail_silently=False)
            sent = True
            cd = form.cleaned_data
            # ... send email
    else:
        form = EmailPostForm()
    return render(request, 'poems/post_share.html', {'post': post,'form': form})


def post_detail(request, year, month, day, post):
    # return HttpResponse('You are in post list')
    post = get_object_or_404(Post, slug=post, 
                                    status='published',
                                    publish__year=year, 
                                    publish__month=month, 
                                    publish__day=day)
    # return HttpResponse('object taken')
    # List of active comments for this post
    comments = post.comments.filter(active=True).order_by('-created')
    new_comment = None
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'poems/post_detail.html', {'post':post,
                                                        'comments': comments,
                                                        'new_comment': new_comment,
                                                        'comment_form': comment_form}) 


class GalleryView(ListView):
    queryset = Photo.objects.all().order_by('-date')
    context_object_name = 'images'
    paginate_by = 50
    template_name = 'poems/cards-gallery.html'




# def poems_view(request):
#     poem = Poem.objects.all().order_by('-date')
#     paginator = Paginator(poem, 3) # 3 posts in each page
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer deliver the first page
#         posts = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range deliver last page of results
#         posts = paginator.page(paginator.num_pages)
#     return render(request, 'poems/poem_list.html', {'poem':poem})

class PoemListView(ListView):
    queryset = Poem.objects.all().order_by('-date')
    context_object_name = 'poem'
    paginate_by = 3
    template_name = 'poems/poem_list.html'
  
