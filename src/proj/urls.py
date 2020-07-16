"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from genre.views import Test, CreateGenre, UpdateGenre, ListGenre, DeleteGenre
from books.views import ListGenreBook
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from profiles.views import LoginProfile, LogoutProfile, PasswordChange, PasswordReset, PasswordResetDone, PasswordResetConfirm, PasswordResetComplete



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListGenreBook.as_view(), name='main'),
    path('genre/', include('genre.urls', namespace="genre")),
    path('books/', include('books.urls', namespace="books")),
    path('profiles/', include('profiles.urls', namespace="profiles")),
    path('authors/', include('authors.urls', namespace="authors")),
    path('cart/', include('cart.urls', namespace="cart")),
    path('order/', include('order.urls', namespace="order")),
    path('login/', LoginProfile.as_view(), name='login'),
    path('logout/', LogoutProfile.as_view(), name='logout'),
    path('password_change/', PasswordChange.as_view(), name='password_change'),
    #path('password_reset/', PasswordReset.as_view(), name='password_reset'),
    #path('password_reset_done/', PasswordResetDone.as_view(), name='password_reset_done'),
    #path('password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    #path('password_reset_complete/', PasswordResetComplete.as_view(), name='password_reset_complete'),
    url(r'^', include('django.contrib.auth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
