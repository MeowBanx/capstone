from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import ClientProfile, EditorProfile, EditingProject
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'brevisapp/index.html')

def registration_page(request):
    return render(request, 'brevisapp/register.html')

def login_page(request):
    return render(request, 'brevisapp/login.html')

def register_user(request):
    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    login(request, user)
    return HttpResponseRedirect(reverse('brevisapp:user_page'))

@login_required
def user_page(request):
    context = {
    }
    return render(request, 'brevisapp/user_page.html', context)


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login_user(request, user)
        return HttpResponseRedirect(reverse('brevisapp:user_page'))
    return HttpResponseRedirect(reverse('brevisapp:login'))



def new_project(request):
    user = User.objects.get(pk=user_id)
    project.name = request.POST['proj_name']
    orig_file = request.POST['orig_file']
    orig_text = request.POST['orig_text']
    description = request.POST['description']
    submit_date = request.POST['submit_date']


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('brevisapp:index'))
