from . import views
from django.urls import path

urlpatterns = [
    path('apply_teacher/', views.apply_teacher, name='apply_teacher'),
    path('get_teacher/', views.get_teacher, name='get_teacher'),
]
