from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm, RegisterForm
from .views import (
    index,
    RegisterView,
    LoginView,
)

app_name = 'users'

urlpatterns = [
    path('', index, name='user-index'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('login/', LoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

]