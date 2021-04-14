from django.urls import path
from . import views

from . import views

app_name = 'ticket'

urlpatterns = [
    path('', views.ticket, name='ticket'),

]
