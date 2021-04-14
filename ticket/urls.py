from django.urls import path
from . import views

from . import views

app_name = 'ticket'

urlpatterns = [
    path('', views.ticket, name='ticket'),
    path('edit/<int:ticket_id_edit>', views.ticket, name='edit_ticket'),
    path('del/<int:ticket_id_del>', views.ticket, name='del_ticket'),

]
