from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_new_member', views.add_new_member, name='membersaved'),
]