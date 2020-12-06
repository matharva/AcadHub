from django.shortcuts import render, redirect
from .forms import *
from .models import *
from login.models import *
from . import models
# Create your views here.

# def postView(request):
#   return render(request, 'index')

def postView(request, post_id): 
  currentPost = Post.objects.get(id=post_id)
  currentPostComments = Comment.objects.filter(post=currentPost).order_by("-post_id")
  currentUserProfile = Profile.objects.get(user=request.user)
  college = currentUserProfile.college.replace(" ", "")
  
  if request.method == 'POST': 
    cf = CommentForm(request.POST or None) 
    if cf.is_valid(): 
      content = request.POST.get('content') 
      if currentPost.community.name == college:
        comment = Comment.objects.create(post = currentPost, user = User.objects.get(username='anonymous'), content = content) 
      else:
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
  currentUserProfile = Profile.objects.get(user=request.user)
  college = currentUserProfile.college.replace(" ", "")
  if request.method == 'POST': 
    pf = PostForm(request.POST or None, request.FILES or None) 
    if pf.is_valid():
      if request.FILES.get('image'):
        newPost = Post(image=request.FILES['image'])
      else:
        newPost = Post()
      if college==community_name:
        newPost.author = User.objects.get(username='anonymous')
      else:
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

def communityView(request, community_name):
  currentCommunity = Community.objects.get(name=community_name) 
  posts = Post.objects.filter(community = currentCommunity)

  context = {
    'community':currentCommunity,
    'posts':posts,
  }

  return render(request, 'post_list.html', context)

def communityCreateView(request):
  comf = CommunityForm(request.POST)
  if request.method == 'POST':
    if comf.is_valid():
      newCom = Community()
      newCom.name = comf.cleaned_data['name']
      newCom.description = comf.cleaned_data['description']
      newCom.save()
      return redirect('index')

  context = {
    'community_form': comf,
  }
  return render(request, 'newCommunity.html', context)

def communityListView(request):
  currentCommunity = Community.objects.all()

  context = {
    'community': currentCommunity, 
  }
  return render(request, 'com_list.html', context)

def projectListView(request):
  projects = ProjectPost.objects.all()
  context = {
    'posts': projects,
  }
  return render(request, 'projectPostList.html', context)

def createProjectPost(request):
  if request.method == 'POST': 
    ppf = ProjectPostForm(request.POST or None, request.FILES or None) 
    if ppf.is_valid():
      if request.FILES.get('image'):
        newPost = ProjectPost(image=request.FILES['image'])
      else:
        newPost = ProjectPost()
      newPost.author = request.user
      newPost.description = ppf.cleaned_data['description']
      newPost.requirements = ppf.cleaned_data['requirements']
      newPost.domain = ppf.cleaned_data['domain']
      newPost.deadline = ppf.cleaned_data['deadline']
      newPost.link = ppf.cleaned_data['link']
      newPost.title = ppf.cleaned_data['title']
      # newPost.image = pf.cleaned_data.get('image', None)
      newPost.save()
      newPost.contributors.add(request.user)
      newPost.save()
      return redirect('postandcomment_app:projectPost', ppost_id = newPost.id) 
  else: 
    ppf = ProjectPostForm() 
    
  context = {
    'post_form':ppf, 
  } 
  return render(request, 'newPost.html', context) 

def projectPostView(request, ppost_id):
  currentPost = ProjectPost.objects.get(id=ppost_id)
  contributors = currentPost.contributors.all()
  currentPostComments = PComment.objects.filter(ppost=currentPost).order_by("-ppost_id")
  currentUserProfile = Profile.objects.get(user=request.user)
  college = currentUserProfile.college.replace(" ", "")
  
  if request.method == 'POST': 
    if 'comment' in request.POST:
      pcf = PCommentForm(request.POST or None) 
      if pcf.is_valid(): 
        content = request.POST.get('content')
        comment = PComment.objects.create(ppost = currentPost, user = request.user, content = content) 
        comment.save() 
        return redirect('postandcomment_app:projectPost', ppost_id = ppost_id) 
    else:
      currentPost.contributors.add(request.user)
      currentPost.save()
      pcf = PCommentForm() 
      contributors = currentPost.contributors.all()
  else: 
    pcf = PCommentForm() 

  if request.user in list(contributors):
    context ={ 
    'formPresent': 'yes',
    'postDetails': currentPost,
    'comments': currentPostComments,
    'contributors': contributors,
    'comment_form':pcf, 
    } 
  else:
    context ={ 
    'formPresent': 'no',
    'postDetails': currentPost,
    'contributors': contributors,
    'comments': currentPostComments,
    } 
  
  return render(request, 'projectPost.html', context)
