from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TicketForm

@login_required(login_url='/account/login')
def ticket(request):
    form = TicketForm()

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            set_ticket = form.save(commit=False)
            set_ticket.user = request.user
            set_ticket.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'ticket.html', context)



