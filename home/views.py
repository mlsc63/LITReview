from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from review.models import Review
from django.http import HttpResponse
from ticket.models import Ticket


from itertools import chain
from django.db.models import CharField, Value
from django.shortcuts import render


@login_required(login_url='/account/login')
def home(request):


    return render(request, 'home.html')


@login_required(login_url='/account/login')
def post(request):
    tickets = Ticket.objects.filter(user=request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    reviews = Review.objects.filter(user=request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )
    return render(request, 'post.html', context={'posts': posts})
