from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from poems.models import Post
from django.urls import reverse

class LatestPostsFeed(Feed):
    title = 'My Blog'
    link = '/poems/'
    description = 'New posts of my blog'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)

    def item_link(self, item):
        return reverse('poems:post_feed', args=[item.pk])
