from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.post, name='post'),
    path('follow/add/<int:follow_id_add>', views.follow, name='add_follow'),
    path('follow/del/<int:follow_id_del>', views.follow, name='del_follow'),
    path('follow/', views.display_user, name='display_user'),
    path('ticket/', views.ticket, name='ticket'),
    path('ticket/edit/<int:ticket_id_edit>', views.ticket, name='edit_ticket'),
    path('ticket/del/<int:ticket_id_del>', views.ticket, name='del_ticket'),
    path('review/', views.add_review, name='review'),
    path('review/edit/<int:review_id_edit>', views.add_review, name='edit_review'),
    path('review/add/<int:review_id_add>', views.add_review, name='add_review'),
    path('review/del/<int:review_id_del>', views.add_review, name='del_review'),
    path('account/login/', views.login_user, name='login'),
    path('account/signup/', views.signup_user, name='signup'),
    path('account/logout/', views.logout_user, name='logout'),

]
