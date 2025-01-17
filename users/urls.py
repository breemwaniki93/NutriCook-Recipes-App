from django.urls import path
from . import views

urlpatterns = [
    # User-specific pages
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('terms-of-service/', views.terms_of_service, name='terms-of-service'),
    path('faqs/', views.faqs, name='faqs'),
]
