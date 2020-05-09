from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('login/', views.user_login, name='login_url'),
    path('', views.dashboard, name='dashboard_url'),
    path('login/', auth_views.LoginView.as_view(), name='login_url'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_url'),
]
