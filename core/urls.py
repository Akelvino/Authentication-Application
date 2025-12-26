from django.urls import path
from . import views
from django.contrib.auth import views as aut_view
from .forms import LoginForm


urlpatterns = [
    path('',views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', aut_view.LoginView.as_view(
        template_name = 'core/login.html', 
        authentication_form = LoginForm,
        redirect_authenticated_user = True,
        next_page = 'home'
        ), 
        name='login'
    ),

    path('logout/', aut_view.LogoutView.as_view(), name='logout')
]