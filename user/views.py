from django.shortcuts import render, redirect
from .models import User
from .forms import UserRegistration, UserLogin
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.template import loader



def login(request):

    form = UserLogin()
    context = {
        'form': form
    }
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(username=email, password=password)
    if user is not None:
        return HttpResponse('Connecté')
    else:
        return render(request, 'login.html', context)


def registration (request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = User.objects.filter(email=email)
        if not contact.exists():
            user = User.objects.create_user(email, email, password)
            user.save()
            context = {
                "registration": "True",
            }
            return render(request, 'login.html', context)
            # return redirect('login')

    form = UserRegistration()
    context = {
        'form': form
    }

    return render(request, 'registration.html', context)





