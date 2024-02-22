from django.urls import path
from . import views

urlpatterns = [
    path('project1app/', views.project1app, name='project1app'),
]