from django.views.generic import FormView, TemplateView, ListView, View
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm, LoginForm
from .models import UserAccount

class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(self.request, user)
        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'registration/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user:
            login(self.request, user)
            return super().form_valid(form)
        form.add_error(None, 'Неверный логин или пароль')
        return self.form_invalid(form)

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/profile.html'

class UsersListView(LoginRequiredMixin, ListView):
    model = UserAccount
    template_name = 'registration/users_list.html'
    context_object_name = 'users'
