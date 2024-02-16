from django.urls import path
from . import views

urlpatterns = [
    path('chatbot/', views.chatbot_response, name='chatbot_response'),
    # Add other URL patterns for your views if needed
]
