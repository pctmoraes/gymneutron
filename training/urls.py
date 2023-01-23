from django.urls import path
from . import views

urlpatterns = [
    path('', views.training, name="training")
]