from django.shortcuts import render
from django.template import Context
from django.http import HttpResponse
from .models import Genre
from .models import Books
from .forms import CreateGenreForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic import ListView
# Create your views here.

class Test(TemplateView):
    template_name='testapp/test.html'
  
    
class CreateGenre(CreateView):
    model=Genre
    form_class=CreateGenreForm
    template_name='testapp/create_genre.html'
    success_url="/test/"

class UpdateGenre(UpdateView):
    model=Genre
    form_class=CreateGenreForm
    template_name='testapp/create_genre.html'
    success_url="/test/"

class ListGenre(ListView):
    model=Genre
    context_object_name = 'genre_list'
    template_name='testapp/list-genre.html'


