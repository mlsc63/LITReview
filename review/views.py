from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/account/login')
def add_review(request):

    return render(request, 'review.html')