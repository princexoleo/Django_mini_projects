from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
# import django decorators
from django.contrib.auth.decorators import login_required

# from users
from .forms import RegisterForm, LoginForm

# Create your views here.
@login_required
def index(request):
    # get profile of login users
    context = {}
    profile = request.user.profile
    context['profile'] = profile
    return render(request, 'users/profile_home.html', context)

# Custom LoginView class
class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
    
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super(LoginView, self).form_valid(form)

# Creates a class based RegisterView
class RegisterView(View):
    form_class= RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form}) 
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            # Get info
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect(to='/')
        
        return render(request, self.template_name, {'form': form})
    
    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)


