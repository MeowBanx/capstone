from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import ClientProfile, EditorProfile, EditingProject, Message
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.mail import send_mail
import PyPDF2
from tika import parser
import string
from django.core.paginator import Paginator

#==========page views=====================================================
def index(request):
    return render(request, 'brevisapp/index.html')


def registration_page(request):
    return render(request, 'brevisapp/register.html')


def login_page(request):
    return render(request, 'brevisapp/login_page.html')


@login_required (login_url='/login_page/')
def user_page(request):
    current_projects = request.user.client.projects.filter(final_date__isnull=True).order_by('submit_date')
    past_projects = request.user.client.projects.filter(final_date__isnull=False).order_by('submit_date')
    context = {
        'current_projects': current_projects,
        'past_projects': past_projects,
    }

    return render(request, 'brevisapp/user_page.html', context)


@login_required (login_url='/login_page/')
def submit(request):
    return render(request, 'brevisapp/submit.html')


def length_error(request, project_id):
    project = get_object_or_404(EditingProject, pk=project_id)
    context = {
        'project': project,
    }
    return render(request, 'brevisapp/length_error.html', context)


def confirmation_page(request, project_id):
    project = get_object_or_404(EditingProject, pk=project_id)
    context = {
        'project': project,
    }
    return render(request, 'brevisapp/confirmation_page.html', context)


def get_a_quote(request):
    return render(request, 'brevisapp/get_a_quote.html')


def FAQs(request):
    return render(request, 'brevisapp/FAQs.html')


@login_required (login_url='/login_page/')
def client_project(request, project_id):
    project = get_object_or_404(EditingProject, pk=project_id)
    messages = project.messages.all()
    context = {
        'project': project,
        'messages': messages
    }
    return render(request, 'brevisapp/client_project.html', context)


@login_required (login_url='/login_page/')
def to_edit(request):
    if not request.user.editor:
        return HttpResponse('get out of here')
    projects = EditingProject.objects.filter(edit_date__isnull=True).order_by('submit_date')
    projects_with_questions = EditingProject.objects.filter(final_date__isnull=True).order_by('submit_date')
    projects_with_questions = [project for project in projects_with_questions if project.messages.count() > 0]
    context = {
        'projects': projects,
        'projects_with_questions': projects_with_questions,
    }
    return render(request, 'brevisapp/to_edit.html', context)


@login_required (login_url='/login_page/')
def edit_project(request, project_id):
    project = get_object_or_404(EditingProject, pk=project_id)
    messages = project.messages.all()
    context = {
        'project': project,
        'messages': messages,
    }
    return render(request, 'brevisapp/edit_project.html', context)


def my_account(request):
    client = request.user.client
    projects = request.user.client.projects.all()
    context = {
        'client': client,
        'projects': projects,
    }
    return render(request, 'brevisapp/my_account.html', context)


#==========form submission views=====================================================

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


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('brevisapp:user_page'))
    else:
        return HttpResponseRedirect(reverse('brevisapp:login_page'))


def new_project(request):
    client = request.user.client
    editor = User.objects.get(username='Admin').editor
    proj_name = request.POST['proj_name']
    project = EditingProject(name=proj_name)
    project.orig_file = request.FILES.get('orig_file', None)
    project.orig_text = request.POST['orig_text']
    project.description = request.POST['description']
    project.submit_date = timezone.now()
    project.client = client
    project.editor = editor
    project.word_count = 0
    project.price = 0
    project.turnaround = 'project_turnaround' in request.POST
    project.save()
    word_count = count_words(project)
    project.word_count = float(word_count)
    project.save()
    if project.turnaround:
        project.price = word_count*0.04
    else:
        project.price = word_count*0.02
    project.save()
    if project.word_count > 5000:
        return HttpResponseRedirect(reverse('brevisapp:length_error', args=[project.id]))
    elif project.word_count > 1000 and project.turnaround:
        return HttpResponseRedirect(reverse('brevisapp:length_error', args=[project.id]))
    else:
        return HttpResponseRedirect(reverse('brevisapp:confirmation_page', args=[project.id]))


def change_turnaround(request, project_id):
    project = get_object_or_404(EditingProject, pk=project_id)
    project.turnaround = False
    project.save()
    return HttpResponseRedirect(reverse('brevisapp:confirmation_page', args=[project.id]))


def confirmed(request, project_id):
    project = get_object_or_404(EditingProject, pk=project_id)
    project.submitted = True
    project.save()
    return HttpResponseRedirect(reverse('brevisapp:user_page'))


def delete_project(request, project_id):
    project = get_object_or_404(EditingProject, pk=project_id)
    project.delete()
    return HttpResponseRedirect(reverse('brevisapp:user_page'))


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


def submit_question(request, project_id):
    message = Message()
    message.editingproject_id = project_id
    message.text = request.POST.get('question_for_editor', '')
    message.user = request.user
    message.timestamp = timezone.now()
    message.save()
    return HttpResponseRedirect(reverse('brevisapp:user_page'))


def submit_answer(request, project_id):
    message = Message()
    message.editingproject_id = project_id
    message.text = request.POST.get('question_for_editor', '')
    message.user = request.user
    message.timestamp = timezone.now()
    message.save()
    project = message.editingproject
    project.edit_text = request.POST.get('edit_text', '')
    project.edit_file = request.FILES.get('edit_file', None)
    project.edit_date = timezone.now()
    project.save()
    return HttpResponseRedirect(reverse('brevisapp:user_page'))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('brevisapp:index'))


#==========functions===========================================================

def count_words(project):
    if project.orig_file:
        file = project.orig_file.path
        # Parse data from file
        file_data = parser.from_file(file)
        # Get files text content
        text = file_data['content']
        text = text.lower() # lowercase all letters
        text = text.replace('“', '"') # replace curly quotes so they are removed in function below
        text = text.replace('”', '"')
        text = text.replace('—', '-') #remove en-dashes
        text = text.replace('  ', ' ') #remove double spaces
        result = ""
        for character in text:
            if character not in string.punctuation:
                result += character
        text = result
        word_list = text.split() #turn string into list of words
        word_count = 0
        for word in word_list:
            word_count += 1
        return word_count
    else:
        text = project.orig_text
        text = text.lower() # lowercase all letters
        text = text.replace('“', '"') # replace curly quotes so they are removed in function below
        text = text.replace('”', '"')
        text = text.replace('—', '-') #remove en-dashes
        text = text.replace('  ', ' ') #remove double spaces
        result = ""
        for character in text:
            if character not in string.punctuation:
                result += character
        text = result
        word_list = text.split() #turn string into list of words
        word_count = 0
        for word in word_list:
            word_count += 1
        return word_count
