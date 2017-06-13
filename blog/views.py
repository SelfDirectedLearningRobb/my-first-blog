from django.shortcuts import render, get_object_or_404, redirect
#import the timezone functionality in order to be able to sort by published date, etc.
from django.utils import timezone
#import the Post class from the models.py file in the same directory 
#(since it is in the same directory we can omit the .py file extension)
from .models import Post
from .forms import PostForm

# Create your views here.

# this function is called by blog/urls.py which is called by mySite/urls.py
# it returns the post_list view located in blog/post_postlist.html 
def post_list(request):
	#create an instance of the blog posts from the Posts class which contains published posts ordered by publication date
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})
	
def post_detail(request, pk):
	#assign an instance 'post' of the 'Post' class as defined in models.py where the post key or pk specifies the specific post
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})
	
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
		return render(request, 'blog/post_edit.html',{'form': form})
		
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})