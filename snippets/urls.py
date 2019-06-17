from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:code_id>/', views.viewCode, name = 'viewCode'),
    path('newCodeSnippet', views.newCodeSnippet, name = 'newCodeSnippet'),
    path('submitNewCodeSnippet', views.submitNewCodeSnippet, name = 'submitNewCodeSnippet'),
    path('edit/<int:code_id>/', views.editCode, name='editCode'),
    path('makeChanges/<int:code_id>', views.makeChanges, name='makeChanges'),
    path('profile/<str:username>', views.showProfile, name='showProfile'),
    path('search', views.search, name='search')
    
]