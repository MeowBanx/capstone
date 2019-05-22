from django.urls import path
from . import views

app_name = 'brevisapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('login_page/', views.login_page, name='login_page'),
    path('registration_page/', views.registration_page, name='registration_page'),
    path('register_user/', views.register_user, name='register_user'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('user_page/', views.user_page, name='user_page'),
    path('submit/', views.submit, name='submit'),
    path('new_project/', views.new_project, name='new_project'),
    path('<int:project_id>/client_project/', views.client_project, name='client_project'),
    path('to_edit/', views.to_edit, name='to_edit'),
    path('<int:project_id>/edit_project/', views.edit_project, name='edit_project'),
    path('<int:project_id>/submit_edit/', views.submit_edit, name='submit_edit'),
    path('get_a_quote/', views.get_a_quote, name='get_a_quote'),
    path('<int:project_id>/approve_edit/', views.approve_edit, name='approve_edit'),
    path('<int:project_id>/confirmation_page/', views.confirmation_page, name='confirmation_page'),
    path('<int:project_id>/confirmed/', views.confirmed, name='confirmed'),
    path('<int:project_id>/delete_project/', views.delete_project, name='delete_project'),
    path('<int:project_id>/submit_question/', views.submit_question, name='submit_question'),
    path('<int:project_id>/submit_answer/', views.submit_answer, name='submit_answer'),
    path('FAQs/', views.FAQs, name='FAQs'),
    path('<int:project_id>/length_error/', views.length_error, name='length_error'),
    path('<int:project_id>/change_turnaround/', views.change_turnaround, name='change_turnaround'),
    path('my_account/', views.my_account, name='my_account'),
]
