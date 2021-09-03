from . import views
from django.urls import path

urlpatterns = [
    path('apply_translator/', views.apply_translator, name='apply_translator'),
    path('get_translator/', views.get_translator, name='get_translator'),
]
