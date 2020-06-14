from django.shortcuts import render
from django.shortcuts import render
from django.template import Context
from django.http import HttpResponse
from .models import Books
from .forms import CreateBookForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

# Create your views here.
class CreateBook(CreateView):
    model=Books
    form_class=CreateBookForm
    template_name='testapp/create_genre.html'
    def get_success_url(self):
       return reverse_lazy('books:list')

class UpdateBook(UpdateView):
    model=Books
    form_class=CreateBookForm
    template_name='testapp/create_genre.html'

    def get_success_url(self):
       return reverse_lazy('books:list')

class ListBook(ListView):
    model=Books
    context_object_name = 'obj'
    template_name='testapp/list-book.html'

class DeleteBook(DeleteView):
    model=Books
    form_class=CreateBookForm
    template_name='testapp/delete_genre.html'
    def get_success_url(self):
       return reverse_lazy('books:list')