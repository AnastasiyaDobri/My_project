from django.urls import path
from django.contrib.auth import views as auth_views
from profiles.views import CreateProfile

from django.contrib.auth import views as auth_views
app_name="profiles"

urlpatterns = [

    path('create/', CreateProfile.as_view(), name='create'),


]