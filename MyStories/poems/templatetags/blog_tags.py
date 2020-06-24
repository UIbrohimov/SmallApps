from django import template
from ..models import Post, Photo
from django.db.models import Count

from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('poems/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-created')[:count]
    return {'latest_posts':latest_posts}

# @register.inclusion_tag('poems/search_result.html')
# def show_search_results():
#     resluts = Post.published.all()
#     return {'results':resluts}

@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))

################ one of the advanteges of django's template taging ##############
# showing a cuple of models' content in one template 
# wothout setting a number of models in one view!
@register.inclusion_tag('poems/gallery.html')
def latest_photos(count=3):
    photos = Photo.objects.all().order_by('-date')[:count]
    return {'photos':photos}