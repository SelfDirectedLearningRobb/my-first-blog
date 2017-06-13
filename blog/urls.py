from django.conf.urls import url
from . import views

#if someone requests the blog directory serve them the post_list view page
urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	#if someone requests a specific post (as defined in the post_detail function in views.py) serve them the post_detail view page
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	#add a link to the Post_Form when the link is clicked to create a new post
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]