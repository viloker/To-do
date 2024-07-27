from django.urls import path

from . import views

urlpatterns = [
    path('', views.check_user, name='check_user'),
    path("log-in/", views.log_in, name='log_in'),
    path('add-task/', views.add_task, name='add_task'),
    path('show-tasks/', views.show_tasks, name='show_tasks'),
    path('delete_task/<str:task>', views.delete_task, name='delete_task')
]
