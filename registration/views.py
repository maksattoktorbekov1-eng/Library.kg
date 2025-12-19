from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
from .models import UserAccount

def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('profile')
            else:
                form.add_error(None, "Неверный логин или пароль")
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')

def profile(request):
    return render(request, 'registration/profile.html')

def users_list(request):
    users = UserAccount.objects.all()
    return render(request, 'registration/users_list.html', {'users': users})