from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from usuarios.forms import RegistroUserForm
from reservas.forms import TrainingReservationForm
from reservas.models import TrainingReservation



def index(request):
    return render(request,'index/index.html',{
    })

def logout_view(request):
    logout(request)
    return redirect('index')

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

def home(request):
    return render(request,'home/home.html',{
    })

def reserve_done(request):
    return render(request, 'reserve/reserve_done.html',{
    })

def reserve(request):
    if request.method == 'POST':
        form = TrainingReservationForm(request.POST)
        if form.is_valid():
            nueva_reserva = form.save(commit=False)
            nueva_reserva.user = request.user
            nueva_reserva.save()
            form.save_m2m()

            return redirect('reserve_done')
    else:
        form = TrainingReservationForm ()

    return render(request,'reserve/reserve.html',{'form':form})

@login_required
def view_reservations(request):
    reservas_del_usuario = TrainingReservation.objects.filter(user=request.user).order_by('date', 'time')
    contexto = {
        'reservas': reservas_del_usuario
    }
    return render(request, 'reserve/view_reservations.html', contexto)