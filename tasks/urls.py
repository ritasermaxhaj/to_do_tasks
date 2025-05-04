from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('auth/register/', views.register, name='register'),
    path('auth/login/', views.login_view, name='login'),
    path('auth/logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('task_form/', views.task_create, name='task_create'),
    path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('task/<int:pk>/toggle/', views.toggle_task_completion, name='toggle_task_completion'),  # Update this line
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
]