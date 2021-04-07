from . import views
from django.urls import path

urlpatterns = [
    path('payment/', views.payment, name='payment'),
]
