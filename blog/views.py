from django.shortcuts import render, get_object_or_404
#import the timezone functionality in order to be able to sort by published date, etc.
from django.utils import timezone
#import the Post class from the models.py file in the same directory 
#(since it is in the same directory we can omit the .py file extension)
from .models import Post

# Create your views here.

# this function is called by blog/urls.py which is called by mySite/urls.py
# it returns the post_list view located in blog/post_postlist.html 
def post_list(request):
	#create an instance of the blog posts from the Posts class which contains published posts ordered by publication date
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})
	
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})