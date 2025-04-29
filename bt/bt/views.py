from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from usuarios.forms import RegistroUserForm

def index(request):
    return render(request,'index/index.html',{
    })

def home(request):
    return render(request,'home/home.html',{
    })

def auth(request):
    if request.method == 'POST':
        if 'register_submit' in request.POST:
            form = RegistroUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data['username']
                return redirect('home')
            else:
                context = {'form': form}
                return render(request, 'auth/auth.html', context)
        elif 'login_submit' in request.POST:
            login_form = AuthenticationForm(request, request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    return render(request, 'auth/auth.html', {'login_form': login_form, 'show_login': True})
            else:
                return render(request, 'auth/auth.html', {'login_form': login_form, 'show_login': True})
    else:
        registro_form = RegistroUserForm()
        login_form = AuthenticationForm()
        context = {'form': registro_form, 'login_form': login_form}
        return render(request, 'auth/auth.html', context)