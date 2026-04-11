from django.urls import path
from . import views

urlpatterns = [
    # UI
    path('tasks/', views.task_page, name='tasks_page'),

    # API
    path('api/tasks/', views.TaskListView.as_view(), name='tasks_api'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
]