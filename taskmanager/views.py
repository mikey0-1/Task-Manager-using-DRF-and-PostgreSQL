from datetime import date

from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions

from .filters import TaskFilter
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

class TaskListView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('due_date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

@login_required
def task_page(request):
    tasks = Task.objects.filter(user=request.user).order_by('due_date')

    task_filter = TaskFilter(request.GET, queryset=tasks)
    tasks = task_filter.qs

    if request.method == 'POST':
        Task.objects.create(
            user=request.user,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
        )
        return redirect('tasks_page')

    return render(request, 'tasks.html', {'tasks': tasks, 'task_filter': task_filter})
