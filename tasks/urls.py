from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks_list, name="tasks_list"),
    path('create_task', views.create_task, name="create_task"),
    path('delete_task/<int:id>/', views.delete_task, name ="delete_task")
]
