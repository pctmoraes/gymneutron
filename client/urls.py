from django.urls import path
from . import views

urlpatterns = [
    path('', views.client, name="client"),
    path('update/', views.update_client, name="update_client")
]