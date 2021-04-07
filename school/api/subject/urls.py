from . import views
from django.urls import path

urlpatterns = [
    path('subject/', views.subject, name='subject'),
]
