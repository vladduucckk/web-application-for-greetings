from django.urls import path
from . import views

urlpatterns = [
    path('', views.greetings_home, name='greetings-home'),
    path('add-greeting/', views.add_greeting, name='greeting-add'),
    path('greeting-email/', views.greeting_email, name='greeting-email'),
]
