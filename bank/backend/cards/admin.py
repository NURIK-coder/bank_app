from django.contrib import admin

from cards.models import Card, Category, Transaction

# Register your models here.

admin.site.register(Card)
admin.site.register(Category)
admin.site.register(Transaction)
