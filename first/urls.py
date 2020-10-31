from django.urls import path
from . import views

urlpatterns = [
    #path('', views.titlesite, name='titlesite'),
    path('', views.home, name='home'),
    path('login', views.login, name='login'),

]