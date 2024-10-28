from django.db import models

from users.models import User


# Create your models here.





class Category(models.Model):
    name = models.CharField('Category', max_length=100)

    def __str__(self):
        return self.name


class Card(models.Model):
    card_num = models.BigIntegerField('Card number')
    deadline = models.CharField('Deadline', max_length=10)
    balance = models.BigIntegerField('Balance', default=0, blank=True)
    bank_name = models.CharField('Bank name', max_length=200, null=True, blank=True)
    is_active = models.BooleanField("Is active", default=True)
    phone = models.CharField('Phone', max_length=20, null=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.id} -{self.card_num}'


class Transaction(models.Model):
    datetime = models.DateTimeField('Datetime', auto_now_add=True)
    quantity = models.IntegerField('Quantity', null=True)
    from_card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True, related_name='from_card')
    to_card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True, related_name='to_card')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.value}'


