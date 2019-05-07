from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import ClientProfile, EditorProfile, EditingProject
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def index(request):
    return render(request, 'brevisapp/index.html')

def registration_page(request):
    return render(request, 'brevisapp/register.html')

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
    ClientProfile.objects.create(user=user)
    return HttpResponseRedirect(reverse('brevisapp:user_page'))

@login_required
def user_page(request):
    projects = request.user.client.projects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'brevisapp/user_page.html', context)

def login_page(request):
    return render(request, 'brevisapp/login.html')

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login_user(request, user)
        return HttpResponseRedirect(reverse('brevisapp:user_page'))
    return HttpResponseRedirect(reverse('brevisapp:login'))

def submit(request):
    return render(request, 'brevisapp/submit.html')

def new_project(request):
    client = request.user.client
    editor = User.objects.get(username='admin').editor
    proj_name = request.POST['proj_name']
    project = EditingProject(name=proj_name)
    # print(request.FILES)
    # print(request.POST)
    # print('='*100)
    project.orig_file = request.FILES.get('orig_file', None)
    project.orig_text = request.POST['orig_text']
    project.description = request.POST['description']
    project.submit_date = timezone.now()
    project.client = client
    project.editor = editor
    project.turnaround = 'project_turnaround' in request.POST
    project.save()
    return HttpResponseRedirect(reverse('brevisapp:user_page'))


def project_page(request, project_id):
    project = get_object_or_404(EditingProject, pk=project_id)
    context = {
        'project': project
    }
    return render(request, 'brevisapp/project_page.html', context)

def to_edit(request):
    projects = EditingProject.objects.order_by('submit_date')
    context = {
        'projects': projects
    }
    return render(request, 'brevisapp/to_edit.html', context)

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('brevisapp:index'))
