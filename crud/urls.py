from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('gender/add', views.add_gender)
]
