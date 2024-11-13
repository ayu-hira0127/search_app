from django.shortcuts import render

# Create your views here.
from django.views import View



from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm

class SignupView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todolist:index')
        return render(request, 'accounts/signup.html', {'form': form})

class CustomLoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('todolist:index')
        return render(request, 'accounts/login.html', {'form': form})

class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('todolist:index')

signup = SignupView.as_view()
user_login = CustomLoginView.as_view()
user_logout = CustomLogoutView.as_view()
