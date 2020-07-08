from django.urls import path
from django.contrib.auth import views as auth_views
from profiles.views import CreateProfile
from profiles.views import CreateUserProfile
from django.contrib.auth import views as auth_views
app_name="profiles"

urlpatterns = [

    path('create/', CreateProfile.as_view(), name='create'),
    path('create2/', CreateUserProfile.as_view(), name='create2')


]