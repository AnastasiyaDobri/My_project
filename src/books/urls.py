from django.urls import path
from books.views import CreateBook, UpdateBook, ListBook, DeleteBook, ListGenreBook, DetailBook, ListBookbyGenre
app_name="books"

urlpatterns = [

    path('create/', CreateBook.as_view(), name='create'),
    path('update/<int:pk>', UpdateBook.as_view(), name='update'),
    path('list/', ListBook.as_view(), name='list'),
    path('delete/<int:pk>', DeleteBook.as_view(), name='delete'),
    path('detail/<int:pk>', DetailBook.as_view(), name='detail'),
    path('list_by_genre/<int:pk>', ListBookbyGenre.as_view(), name='list_by_genre'),

]
