from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from ticket.forms import TicketForm
from django.http import HttpResponse
from .models import Review
from ticket.models import Ticket

@login_required(login_url='/account/login')

def add_review(request, review_id_edit=False, review_id_del=False, review_id_add=False):
    # Modifier une review
    if review_id_edit:
        review = Review.objects.get(id=review_id_edit)
        form2 = ReviewForm(instance=review)
        if request.method == 'POST':
            form2 = ReviewForm(request.POST, instance=review)
            if form2.is_valid():
                form2.save()
                return redirect('/')
        context = {'form2': form2}
        return render(request, 'review.html', context)

    if review_id_del:
        review = Review.objects.get(id=review_id_del)
        review.delete()
        return redirect('/')

    if review_id_add:
        ticket = Ticket.objects.get(id=review_id_add)

        form2 = ReviewForm()
        if request.method == 'POST':
            form2 = ReviewForm(request.POST)
            if form2.is_valid():
                form2.ticket = ticket
                form2.save()
                return redirect('/')
        context = {'form2': form2, 'ticket': ticket}
        return render(request, 'review.html', context)




    # Créer une review et son ticket
    if not review_id_edit and not review_id_del:
        ticket_form = TicketForm()
        review_form = ReviewForm()
        if request.method == 'POST':
            form1 = TicketForm(request.POST, request.FILES)
            form2 = ReviewForm(request.POST)
            if form1.is_valid() and form2.is_valid():

                set_ticket = form1.save(commit=False)
                set_ticket.user = request.user

                set_rewiew = form2.save(commit=False)
                set_rewiew.ticket = set_ticket
                set_rewiew.user = request.user

                set_ticket.save()
                set_rewiew.save()
                return redirect('/')

        context = {'form1': ticket_form, 'form2': review_form}
        return render(request, 'review.html', context)

