from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import ClientProfile, EditorProfile, EditingProject
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.mail import send_mail

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
    current_projects = EditingProject.objects.filter(final_date__isnull=True).order_by('submit_date')
    past_projects = EditingProject.objects.filter(final_date__isnull=False).order_by('submit_date')
    context = {
        'current_projects': current_projects,
        'past_projects': past_projects,
    }
    return render(request, 'brevisapp/user_page.html', context)

def login_page(request):
    return render(request, 'brevisapp/login_page.html')

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('brevisapp:user_page'))
    else:
        return HttpResponseRedirect(reverse('brevisapp:login_page'))

def submit(request):
    return render(request, 'brevisapp/submit.html')

def new_project(request):
    client = request.user.client
    editor = User.objects.get(username='admin').editor
    proj_name = request.POST['proj_name']
    project = EditingProject(name=proj_name)
    project.orig_file = request.FILES.get('orig_file', None)
    project.orig_text = request.POST['orig_text']
    project.description = request.POST['description']
    project.submit_date = timezone.now()
    project.client = client
    project.editor = editor
    project.turnaround = 'project_turnaround' in request.POST
    project.save()
    return HttpResponseRedirect(reverse('brevisapp:user_page'))

def get_a_quote(request):
    return render(request, 'brevisapp/get_a_quote.html')


def client_project(request, project_id):
    project = get_object_or_404(EditingProject, pk=project_id)
    context = {
        'project': project
    }
    return render(request, 'brevisapp/client_project.html', context)

def to_edit(request):
    if not request.user.editor:
        return HttpResponse('get out of here')
    projects = EditingProject.objects.filter(edit_date__isnull=True).order_by('submit_date')
    context = {
        'projects': projects
    }
    return render(request, 'brevisapp/to_edit.html', context)

def edit_project(request, project_id):
    project = get_object_or_404(EditingProject, pk=project_id)
    context = {
        'project': project
    }
    return render(request, 'brevisapp/edit_project.html', context)

def submit_edit(request, project_id):
    project = get_object_or_404(EditingProject, pk=project_id)
    project.edit_text = request.POST.get('edit_text', '')
    project.edit_file = request.FILES.get('edit_file', None)
    project.edit_date = timezone.now()
    project.save()
    return HttpResponseRedirect(reverse('brevisapp:to_edit'))

def approve_edit(request, project_id):
    project = get_object_or_404(EditingProject, pk=project_id)
    project.final_date = timezone.now()
    project.save()
    return HttpResponseRedirect(reverse('brevisapp:user_page'))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('brevisapp:index'))
