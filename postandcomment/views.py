from django.shortcuts import render, redirect
from .forms import CommentForm, PostForm
from .models import Comment, Post, Community
from . import models
# Create your views here.

# def postView(request):
#   return render(request, 'index')

def postView(request, post_id): 
  currentPost = Post.objects.get(id=post_id)
  currentPostComments = Comment.objects.filter(post=currentPost).order_by("-post_id")
  
  if request.method == 'POST': 
    cf = CommentForm(request.POST or None) 
    if cf.is_valid(): 
      content = request.POST.get('content') 
      comment = Comment.objects.create(post = currentPost, user = request.user, content = content) 
      comment.save() 
      return redirect('postandcomment_app:post', post_id = post_id) 
  else: 
    cf = CommentForm() 
    
  context ={ 
    'postDetails': currentPost,
    'comments': currentPostComments,
    'comment_form':cf, 
    } 
  return render(request, 'post.html', context)

def postCreateView(request, community_name):
  currentCommunity = Community.objects.get(name=community_name)

  if request.method == 'POST': 
    pf = PostForm(request.POST or None, request.FILES or None) 
    if pf.is_valid():
      if request.FILES.get('image'):
        newPost = Post(image=request.FILES['image'])
      else:
        newPost = Post()
      newPost.author = request.user
      newPost.community = currentCommunity
      newPost.content = pf.cleaned_data['content']
      newPost.category = pf.cleaned_data['category']
      newPost.link = pf.cleaned_data['link']
      newPost.title = pf.cleaned_data['title']
      # newPost.image = pf.cleaned_data.get('image', None)
      newPost.save()
      return redirect('postandcomment_app:post', post_id = newPost.id) 
  else: 
    pf = PostForm() 
    
  context = {
    'post_form':pf, 
  } 
  return render(request, 'newPost.html', context) 
