from django.conf.urls import url
from . import views

#if someone requests the blog directory serve them the post_list view page
urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]