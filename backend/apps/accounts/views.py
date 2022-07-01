from django.shortcuts import render, redirect
from django.views.generic import (FormView, CreateView, TemplateView, UpdateView)
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import User
from .forms import LoginForm, UserRegisterForm
from .forms import UserUpdateForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    def form_valid(self, form):
        data = form.cleaned_data
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('index')
            else:
                return HttpResponse('Ваш аккаунт неактивен')
        return HttpResponse('Такого юзера не существует')


class UserRegisterView(CreateView):
    template_name = "register.html"
    form_class = UserRegisterForm

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
            return redirect('index')
        return super(UserRegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(UserRegisterView, self).get(*args, **kwargs)



class RegisterDoneView(TemplateView):
    template_name = "register_done.html"


def user_logout(request):
    if request.user.is_authenticated:
        logout(request.user)
    return redirect('index')


