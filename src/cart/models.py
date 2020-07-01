from django.db import models
from books.models import Books
from django.contrib.auth import get_user_model
User=get_user_model()

class Cart(models.Model):
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='carts',
    )

    def __str__(self):
     return f'Cart #{self.pk}'

class BooksInCart(models.Model):
    cart=models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='books',
    )
    book=models.ForeignKey(
        Books,
        on_delete=models.CASCADE,
        related_name='books_in_cart',
    )
    quantity=models.IntegerField(
        verbose_name="Количество",
        default=1
    )
    def __str__(self):
     return f'Book #{self.book.name}'

    class Meta:
     unique_together = [['cart', 'book']]