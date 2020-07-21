from django.shortcuts import render
from django.template import Context
from django.http import HttpResponse
from books.models import Books
from genre.models import Genre
from comments.models import CommentsBook
from comments.forms import CommentForm
from authors.models import Authors
from .forms import CreateBookForm
from django.views.generic.edit import FormMixin
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from profiles.models import User
from django.http import HttpResponseRedirect

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


        
class DetailBook(FormMixin, DetailView):
    model=Books
    template_name='books/detail-book.html'
    form_class = CommentForm
    def get_object(self):
        book = get_object_or_404(Books, pk=self.kwargs.get('pk'))
        #comments=add_comment(self.request, book.pk)
        return book
    def get_success_url(self):
        return reverse('books:detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(DetailBook, self).get_context_data(**kwargs)
        self.book = get_object_or_404(Books, pk=self.kwargs.get('pk'))
        #context['comments'] = CommentsBook.objects.filter(book=self.book)
        context['form_comments'] = CommentForm(initial={'book': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
            
    def form_valid(self, form):
        user=self.request.user
        form_body=form.cleaned_data['body']
        create=CommentsBook.objects.get_or_create(
            user=str(user),
            book=get_object_or_404(Books, pk=self.kwargs.get('pk')),
            body=form_body,        
        )
        #if create:
            #comment.save(force_insert=True)
        def get_success_url(self):
            return reverse_lazy('books:detail', kwargs={'pk': self.object.pk})

        return HttpResponseRedirect(get_success_url(self))
     


    


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


