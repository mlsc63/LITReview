from django.contrib import admin
from account.models import Account
from review.models import Review
from ticket.models import Ticket
from user_follows.models import UserFollows


admin.site.register(Account)
admin.site.register(Review)
admin.site.register(Ticket)
admin.site.register(UserFollows)