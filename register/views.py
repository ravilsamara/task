from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse
from django.views import View
from django.views.generic import FormView, CreateView
from register.forms import CustomUserCreationForm

class RegisterView(FormView):
    form_class = CustomUserCreationForm
    success_url = '/'
    template_name = 'register/register.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(FormView):
    form_class = AuthenticationForm
    success_url = '/'
    template_name = 'register/login.html'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super().form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('index'))
