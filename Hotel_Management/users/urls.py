from django.urls import path
from . import views

urlpatterns = [path("", views.index, name='index'),
               path("user_register1", views.user_register1, name='user_register1'),
               path("staff_register", views.staff_register, name='staff_register')]