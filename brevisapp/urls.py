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
]
