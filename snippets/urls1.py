from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="redirectToHome"),
    path('<int:code_id>', views.viewCode, name = 'redirectToCode'),
    
    
]