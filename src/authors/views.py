from django.shortcuts import render
from django.shortcuts import render
from django.template import Context
from django.http import HttpResponse
from authors.models import Authors
from books.models import Books
from .forms import CreateAuthorsForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

# Create your views here.
class CreateAuthor(CreateView):
    model=Authors
    form_class=CreateAuthorsForm
    template_name='authors/create_authors.html'
    def get_success_url(self):
       return reverse_lazy('authors:list')

class UpdateAuthor(UpdateView):
    model=Authors
    form_class=CreateAuthorsForm
    template_name='authors/create_authors.html'

    def get_success_url(self):
       return reverse_lazy('authors:list')

class ListAuthor(ListView):
    model=Authors
    context_object_name = 'obj'
    template_name='authors/list-authors.html'

class DetailAuthor(DetailView):
    model=Authors
    template_name='authors/detail-authors.html'


class DeleteAuthor(DeleteView):
    model=Authors
    form_class=CreateAuthorsForm
    template_name='authors/delete_authors.html'
    def get_success_url(self):
       return reverse_lazy('authors:list')

    

