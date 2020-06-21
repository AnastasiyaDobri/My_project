from django.urls import path
from django.contrib.auth import views as auth_views
from profiles.views import CreateProfile
from profiles.views import LoginProfile, LogoutProfile
app_name="profiles"

urlpatterns = [

    path('create/', CreateProfile.as_view(), name='create'),
    path('login/', LoginProfile.as_view(), name='login'),
    path('logout/', LogoutProfile.as_view(), name='logout')

]