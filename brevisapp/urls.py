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
]
