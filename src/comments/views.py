from django.shortcuts import render
from books.models import Books
from django.views.generic.edit import UpdateView
from .models import CommentsBook, CommentsOrder
from .forms import CommentForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic.edit import DeleteView

class CreateComment(UpdateView):
    model=CommentsBook
    form_class=CommentForm
    #template_name='comments/add_comment.html'
    template_name='books/templates/books/detail-book.html'
    def get_object(self):
        book = get_object_or_404(Books, pk=self.kwargs.get('pk'))
        user=self.request.user
        obj, create=self.model.objects.get_or_create(
            book=book,
            user=user,
            body="Your comment",
  )
        return obj
    #book = book
        #if request.method == "POST":
            #form = CommentForm(request.POST)
            #if form.is_valid():
                #comment = form.save(commit=False)
                #comment.book = book
                #comment.save()
                #return redirect('main', pk=book.pk)
        #else:
            #form = CommentForm()
        #return render(request, 'comments/add_comment.html', {'form': form})
    def get_success_url(self):
       return reverse_lazy('main')

class DeleteComment(DeleteView):
    model=CommentsBook
    form_class=CommentForm
    template_name='comments/delete_comment.html'
    def get_success_url(self):
        return reverse_lazy('books:detail', kwargs={'pk': self.object.pk})