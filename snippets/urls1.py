from django.urls import path

from . import views

urlpatterns = [
    path('', views.redirectToHome, name="redirectToHome"),
    path('<int:codeid>', views.redirectToCode, name = 'redirectToCode'),
    
    
]