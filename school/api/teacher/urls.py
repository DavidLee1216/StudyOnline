from . import views
from django.urls import path

urlpatterns = [
    path('apply_teacher/', views.apply_teacher, name='apply_teacher'),
]
