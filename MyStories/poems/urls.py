from poems import views
from django.urls import path
# from django.views.generic import list_detail
# importing syndication function
from .feeds import LatestPostsFeed

app_name = 'poems'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('poems_view/', views.PoemListView.as_view(), name='poems_view'),
    path('gallery_view/', views.GalleryView.as_view(), name='gallery_view'),
    path('search_result/', views.SearchResultView.as_view(), name='search_result'),
    # url(r'^post_detail/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[\w-])/$', views.post_detail,name='post_detail'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail,name='post_detail'), 
    path('post_share/<int:id>/', views.post_share, name='post_share'),
    # url(r'^poems_view/$', views.poems_view, name='poems_view'), 
    # path('<id>/feed/', LatestPostsFeed(), name='post_feed'),
    path('post_share/', views.post_share, name='post_share'),
]