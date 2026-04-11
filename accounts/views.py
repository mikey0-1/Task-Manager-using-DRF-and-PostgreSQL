from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

def register_page(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/login/')

    return render(request, 'register.html', {'form': form})