from django.shortcuts import render, redirect
from .forms import UserSignup, UserLogin
from django.contrib.auth import authenticate, login, logout


def signup_user(request):
    form = UserSignup()
    if request.method == 'POST':
        form = UserSignup(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/login')
    context = {'form': form}
    return render(request, 'signup.html', context)


def login_user(request):
    form = UserLogin()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('/account/login')
