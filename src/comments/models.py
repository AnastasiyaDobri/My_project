from django.db import models
from books.models import Books
from order.models  import Order

class CommentsBook(models.Model):
    book = models.ForeignKey(Books, related_name='comments', on_delete=models.PROTECT)
    user = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body

class CommentsOrder(models.Model):
    order = models.ForeignKey(Order, related_name='comments', on_delete=models.PROTECT)
    user = models.CharField(max_length=80)
    body = models.TextField(blank=True, help_text='Примечания к заказу')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body