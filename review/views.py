from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from ticket.forms import TicketForm
from django.http import HttpResponse

@login_required(login_url='/account/login')

def add_review(request):
    ticket_form = TicketForm()
    review_form = ReviewForm()
    if request.method == 'POST':
        form1 = TicketForm(request.POST)
        form2 = ReviewForm(request.POST)
        if form1.is_valid() and form2.is_valid():

            set_ticket = form1.save(commit=False)
            set_ticket.user = request.user

            set_rewiew = form2.save(commit=False)
            set_rewiew.ticket = set_ticket
            set_rewiew.user = request.user

            set_ticket.save()
            set_rewiew.save()
            return HttpResponse("ok")

    context = {'form1': ticket_form, 'form2': review_form}
    return render(request, 'review.html', context)

