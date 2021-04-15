from django.urls import path

from . import views

app_name = 'follow'

urlpatterns = [
    path('add/<int:follow_id_add>', views.follow, name='add_follow'),
    path('del/<int:follow_id_del>', views.follow, name='del_follow'),
    path('', views.display_user, name='display_user'),
]
