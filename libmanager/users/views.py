from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from users.models import User
from users.forms import *


class UserHome(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'
    extra_context = {'title': 'Список читателей'}


def get_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)

    context = {"title":"User's profile",
               "user": user}

    return render(request, 'users/profile.html', context=context)

def adduser(request: HttpRequest):
    if request.method == "POST":
        form = AddUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = AddUserForm()
        return render(request, "users/user_form.html", {"form": form, "title": "Add user", "btn_title": "Добавить читателя"})

def deluser(request):
    return HttpResponse("Delete user")

def finduser(request):
    if request.method == 'POST':
        form = FindUserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            fio = form.cleaned_data['fio']
            users = User.objects.filter(fio=fio)
            return render(request, "books/search.html", {"title": "Результаты поиска", "users": users})
    else:
        form = FindUserForm()
    return render(request, "users/user_form.html", {"title": "Найти читателя", "form": form, "btn_title": "Найти читателя"})


def debtors(request):
    return HttpResponse('Shows list of debtors')

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy('login')

class LoginUser(CreateView):
    pass