from django.contrib import admin
from django.urls import path, include
from genre.views import Test, CreateGenre, UpdateGenre, ListGenre, DeleteGenre
app_name="genre"


urlpatterns = [

    path('create/', CreateGenre.as_view(), name='create'),
    path('update/<int:pk>', UpdateGenre.as_view(), name='update'),
    path('list/', ListGenre.as_view(), name='list'),
    path('delete/<int:pk>', DeleteGenre.as_view(), name='delete')
]
