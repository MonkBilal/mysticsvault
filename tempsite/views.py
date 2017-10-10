from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import CommentForm
from django.utils import timezone


def index(request):
	posts =Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'tempsite/index.html',{'posts':posts})

def post_detail(request,pk):
	post =get_object_or_404(Post, pk=pk)
	return render(request,'tempsite/post_detail.html',{'post':post})

def add_comment(request,pk):
	post=get_object_or_404(Post, pk=pk)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = CommentForm()
	return render(request,'tempsite/add_comment.html',{'form':form})			