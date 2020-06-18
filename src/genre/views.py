from django.shortcuts import render
from django.template import Context
from django.http import HttpResponse
from .models import Genre
#from .models import Books
from .forms import CreateGenreForm
#from .forms import CreateBookForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
# Create your views here.

class Test(TemplateView):
    template_name='genre/test.html'

  
    
class CreateGenre(CreateView):
    model=Genre
    form_class=CreateGenreForm
    template_name='genre/create_genre.html'
    def get_success_url(self):
       return reverse_lazy('genre:list')

class UpdateGenre(UpdateView):
    model=Genre
    form_class=CreateGenreForm
    template_name='genre/create_genre.html'

    def get_success_url(self):
       return reverse_lazy('genre:list')

class ListGenre(ListView):
    model=Genre
    context_object_name = 'obj'
    template_name='genre/list-book.html'

class DeleteGenre(DeleteView):
    model=Genre
    form_class=CreateGenreForm
    template_name='genre/delete_genre.html'
    def get_success_url(self):
       return reverse_lazy('list')

