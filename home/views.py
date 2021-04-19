from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import UserSignup, UserLogin
from django.contrib.auth import authenticate, login, logout
from .models import UserFollows, Ticket, Review, Account
from .forms import TicketForm, ReviewForm
from itertools import chain
from django.db.models import CharField, Value
from django.shortcuts import render


@login_required(login_url='/account/login')
def home(request):
    friends = UserFollows.objects.filter(user=request.user).select_related("followed_user")
    friend = [user.followed_user for user in friends]
    friend.append(request.user)
    print(friend)

    # ticket seul
    ticket = Ticket.objects.filter(user__in=friend)
    ticket = ticket.filter(user__in=friend, review__ticket__isnull=True)
    ticket = ticket.annotate(content_type=Value('TICKET', CharField()))

    ticket2 = Ticket.objects.filter(user__in=friend)
    reviews_and_ticket = Review.objects.filter(ticket__in=ticket2)

    for add_ticket in reviews_and_ticket:
        get_ticket = Ticket.objects.filter(id=add_ticket.id)
        add_ticket = {'ticket': get_ticket}
    reviews_and_ticket = reviews_and_ticket.annotate(content_type=Value('REVIEW_TICKET', CharField()))

    posts = sorted(
        chain(ticket, reviews_and_ticket),
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


@login_required(login_url='/account/login')
def follow(request, follow_id_add=False, follow_id_del=False):
    if follow_id_add:
        user_to_follow = Account.objects.get(id=follow_id_add)
        test = UserFollows(followed_user=user_to_follow, user=request.user)
        test.save()
        return redirect('/follow')

    if follow_id_del:
        user_followed = Account.objects.get(id=follow_id_del)
        user_to_unfollow = UserFollows.objects.get(user=request.user, followed_user=user_followed)
        user_to_unfollow.delete()
        return redirect('/follow')


@login_required(login_url='/account/login')
def display_user(request):
    # Recherche d'un contact
    if request.method == 'POST':
        username = request.POST.get('recherche')
        user_search = Account.objects.filter(username=username)
        search = {'user_search': user_search}
        return render(request, 'display_user.html', search)

    # Affichage des gens qui suivent
    user_follow = UserFollows.objects.filter(user=request.user)
    followed = UserFollows.objects.filter(followed_user=request.user)

    context = {'user_follow': user_follow, 'followed': followed}
    return render(request, 'display_user.html', context)


@login_required(login_url='/account/login')
def ticket(request, ticket_id_edit=False, ticket_id_del=False):
    if ticket_id_edit:
        ticket = Ticket.objects.get(id=ticket_id_edit)
        form = TicketForm(instance=ticket)
        if request.method == 'POST':
            form = TicketForm(request.POST, request.FILES, instance=ticket)
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
            form = TicketForm(request.POST, request.FILES)
            if form.is_valid():
                set_ticket = form.save(commit=False)
                set_ticket.user = request.user
                set_ticket.save()
                return redirect('/')

        context = {'form': form}
        return render(request, 'ticket.html', context)


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
