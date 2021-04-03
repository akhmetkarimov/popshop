from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/registration', views.register),
    path('auth/create_user', views.create_new),
]