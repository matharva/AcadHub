from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .models import *
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from postandcomment.models import *
# Create your views here.


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('login_app:register')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				user.refresh_from_db()
				# user.userprofile.user = authenticate(username=username, password=password)
				user.save()
				college = form.cleaned_data.get('college')
				if college not in list(Profile.objects.values_list('college', flat=True)):
					newCommunity = Community()
					newCommunity.name = college.replace(" ", "")
					newCommunity.description = f"Incognito Community of {college}"
					newCommunity.save()
					newCommunity.user.add(user)
					newCommunity.save()
				else:
					community = Community.objects.get(name = college.replace(" ", ""))
					community.user.add(user)
				first_name = form.cleaned_data.get('first_name')
				username = form.cleaned_data.get('username')
				password = form.cleaned_data.get('password1')
				user = authenticate(username=username, password=password)
				
				profile = Profile()
				profile.user = user
				profile.college = form.cleaned_data.get('college')
				profile.occupation = form.cleaned_data.get('occupation')
				profile.age = form.cleaned_data.get('age')
				profile.field_of_study = form.cleaned_data.get('field_of_study')
				profile.save()

				login(request, user)
				messages.success(request, 'Account was created for ' + first_name)

				return redirect('login_app:login')
			

		context = {'form':form}
		return render(request, 'login/register.html', context)


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				
				return redirect('index')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login_app:login')
	 
def profile(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			u_form = UserUpdateForm(request.POST, instance=request.user)
			p_form = ProfileUpdateForm(request.POST,
									request.FILES,
									instance=request.user.profile)
			if u_form.is_valid() and p_form.is_valid():
				u_form.save()
				p_form.save()
				messages.success(request, f'Your account has been updated!')
				return redirect('index')

		else:
			u_form = UserUpdateForm(instance=request.user)
			p_form = ProfileUpdateForm(instance=request.user.profile)
			print(u_form, p_form)

		context = {
			'u_form': u_form,
			'p_form': p_form
		}

		return render(request, 'login/profile.html', context)

	else:
		return redirect('index')
	
def profilepage(request,name):

	if request.user.is_authenticated:

		if request.user.username != name:
			value = False
		else:
			value = True

		user = User.objects.get(username = name)
		profile = Profile.objects.get(user = user)
		posts = Post.objects.filter(author = user)
		projectposts = ProjectPost.objects.filter(author = user)
		context = {
			'value':value,
			'user':user,
			'profile':profile,
			'posts':posts,
			'projectposts':projectposts
		}
	return render(request, 'login/profilepage.html', context)
		