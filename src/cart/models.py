from django.db import models
from books.models import Books
from django.contrib.auth import get_user_model
User=get_user_model()

class Cart(models.Model):
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='carts',
        null=True
    )
 
    def __str__(self):
     return f'Cart #{self.pk}'

    @property
    def price(self):
        price=0
        for product in self.books.all():
            price+=product.price
        return price



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
        default=1,

    )
    @property
    def price(self):
        price=self.quantity*self.book.price
        return price

    def __str__(self):
     return f'Book #{self.book.name}'

    class Meta:
     unique_together = [['cart', 'book']]