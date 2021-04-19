from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    path('', views.add_review, name='review'),
    path('edit/<int:review_id_edit>', views.add_review, name='edit_review'),
    path('add/<int:review_id_add>', views.add_review, name='add_review'),
    path('del/<int:review_id_del>', views.add_review, name='del_review'),
]
