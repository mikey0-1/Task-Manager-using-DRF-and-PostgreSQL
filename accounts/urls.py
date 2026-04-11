from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from .views import RegisterUserView, register_page
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # UI
    path('register/', views.register_page, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # API
    path('api/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/register/', RegisterUserView.as_view(), name='api_register'),
]