from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('customerRegister/', views.customerRegister.as_view(), name='customerRegister'),
    path('businessRegister/', views.businessRegister.as_view(), name='businessRegister'),
]
