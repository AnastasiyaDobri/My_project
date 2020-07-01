from django.urls import path
from authors.views import CreateAuthor, UpdateAuthor, ListAuthor, DetailAuthor, DeleteAuthor
app_name="authors"

urlpatterns = [

    path('create/', CreateAuthor.as_view(), name='create'),
    path('update/<int:pk>', UpdateAuthor.as_view(), name='update'),
    path('list/', ListAuthor.as_view(), name='list'),
    path('detail/<int:pk>', DetailAuthor.as_view(), name='detail'),
    path('delete/<int:pk>', DeleteAuthor.as_view(), name='delete'),


]