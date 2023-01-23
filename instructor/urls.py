from django.urls import path
from . import views

urlpatterns = [
    path('', views.instructor, name="instructor"),
    path('update/', views.update_instructor, name="update_instructor")
]