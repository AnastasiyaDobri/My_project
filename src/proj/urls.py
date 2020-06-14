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
from testapp.views import Test, CreateGenre, UpdateGenre, ListGenre, DeleteGenre


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-genre/', CreateGenre.as_view(), name='create-genre'),
    path('test/', Test.as_view(), name='test'),
    path('update-genre/<int:pk>', UpdateGenre.as_view(), name='update-genre'),
    path('list-genre/', ListGenre.as_view(), name='list-genre'),
    path('delete-genre/<int:pk>', DeleteGenre.as_view(), name='delete-genre'),
    path('books/', include('books.urls', namespace="books"))
]
