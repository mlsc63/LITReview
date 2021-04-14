from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/account/login')
def ticket(request):

    return render(request, 'ticket.html')