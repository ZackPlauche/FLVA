from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('contact/thank-you/', views.thank_you, name="thank_you"),
    path('faq/', views.faq, name="faq"),
]
