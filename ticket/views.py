from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TicketForm
from .models import Ticket

@login_required(login_url='/account/login')
def ticket(request, ticket_id_edit=False, ticket_id_del=False ):
    if ticket_id_edit:
        ticket = Ticket.objects.get(id=ticket_id_edit)
        form = TicketForm(instance=ticket)
        if request.method == 'POST':
            form = TicketForm(request.POST, instance=ticket)
            if form.is_valid():
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'ticket.html', context)



    if ticket_id_del:
        ticket = Ticket.objects.get(id=ticket_id_del)
        ticket.delete()
        return redirect('/')


    # On créer un nouveau ticket
    if not ticket_id_edit and not ticket_id_del:
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



