from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserFollows
from account.models import Account

@login_required(login_url='/account/login')
def follow(request, follow_id_add=False, follow_id_del=False ):

    if follow_id_add:
        user_to_follow = Account.objects.get(id=follow_id_add)
        test = UserFollows(followed_user=user_to_follow, user=request.user)
        test.save()
        return redirect('/follow')

    if follow_id_del:
        user_followed = Account.objects.get(id = follow_id_del)
        user_to_unfollow = UserFollows.objects.get(user = request.user, followed_user=user_followed)
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
