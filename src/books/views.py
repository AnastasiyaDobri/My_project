from django.shortcuts import render
from django.shortcuts import render
from django.template import Context
from django.http import HttpResponse
from books.models import Books
from genre.models import Genre
from authors.models import Authors
from .forms import CreateBookForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

# Create your views here.
class CreateBook(CreateView):
    model=Books
    form_class=CreateBookForm
    template_name='books/create_book.html'
    def get_success_url(self):
       return reverse_lazy('books:list')
    def get_success_message(self,*args, **kwargs):
       return f"Книга {self.object.name} была создана"

class UpdateBook(UpdateView):
    model=Books
    form_class=CreateBookForm
    template_name='books/create_book.html'

    def get_success_url(self):
       return reverse_lazy('books:list')

class ListBook(ListView):
    model=Books
    context_object_name = 'obj'
    template_name='books/list-book.html'
    paginate_by = 12
   
class DeleteBook(DeleteView):
    model=Books
    form_class=CreateBookForm
    template_name='books/delete_book.html'
    def get_success_url(self):
       return reverse_lazy('books:list')

class ListGenreBook(ListView):
    model=Books
    context_object_name = 'obj'
    template_name='genre/list-main.html'
    def get_queryset(self):
        queryset={'top': Books.objects.order_by('-rate')[:6],
        'new': Books.objects.order_by('-add_date')[:6]


        }
        return queryset
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['genre'] = Genre.objects.all()
            return context

        
class DetailBook(DetailView):
    model=Books
    template_name='books/detail-book.html'


class ListBookbyGenre(ListView):
    template_name='books/list-book.html'
    def get_queryset(self):
        self.genre = get_object_or_404(Genre, pk=self.kwargs.get('pk'))
        return Books.objects.filter(genre=self.genre)

class ListBookbyAuthor(ListView):
    template_name='books/list-book.html'
    def get_queryset(self):
        self.author = get_object_or_404(Authors, pk=self.kwargs.get('pk'))
        return Books.objects.filter(author=self.author)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = Authors.objects.all()
        return context


