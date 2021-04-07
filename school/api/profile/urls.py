from . import views
from django.urls import include, path
from rest_framework import routers
from .views import ProfileView

urlpatterns = [
    # path('profile/set/', views.set_profile, name='set_profile'),
    path('profile/set/', views.ProfileView.as_view(), name='set_profile'),
    path('profile/get/', views.get_profile, name='get_profile'),
    # path('profile/photo/', views.UploadProfilePhotoView.as_view(),
    #      name='upload_profile_photo'),
]
