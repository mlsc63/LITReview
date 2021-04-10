from django.urls import path

from . import views
app_name = 'user'
urlpatterns = [
    path('', views.login, name='connection'),
    path('registration/', views.registration, name='registration'),

]
