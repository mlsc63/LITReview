from django.contrib.auth.decorators import login_required
from review.models import Review
from ticket.models import Ticket
from user_follows.models import UserFollows



from itertools import chain
from django.db.models import CharField, Value
from django.shortcuts import render


@login_required(login_url='/account/login')
def home(request):
    friends = UserFollows.objects.filter(user=request.user).select_related("followed_user")
    friend = [user.followed_user for user in friends]
    friend.append(request.user)

    ticket = Ticket.objects.filter(user__in=friend, review__ticket__isnull=True )
    ticket = ticket.annotate(content_type=Value('TICKET', CharField()))

    review = Review.objects.filter(user__in=friend)
    review = review.annotate(content_type=Value('REVIEW', CharField()))

    print(ticket)
    posts = sorted(
        chain(review, ticket),
        key=lambda post: post.time_created,
        reverse=True
    )

    return render(request, 'home.html', context={'posts': posts})


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
    return render(request, 'home.html', context={'posts': posts})
