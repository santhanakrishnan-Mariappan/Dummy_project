from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('regiter/', regiter, name='regiter'),
    path('get_all_record/', get_all_record, name='get_all_record'),
    path('get_filter_record/', get_filter_record, name='get_filter_record'),
    path('get_particular_record/', get_particular_record, name='get_particular_record'),
    path('update_record/<str:x>', update_record, name='update_record'),
    path('delete_record/<str:x>', delete_record, name='delete_record'),
    path('send_mail', send_mail, name='send_mail'),
    path('submit/', submit, name='submit'),
]