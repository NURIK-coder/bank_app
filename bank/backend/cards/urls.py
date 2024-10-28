from django.urls import path

from cards.views import CardsListApiView, CategoryListApiView, \
    TransactionListApiView, CreateTransactionApiView, CreateCardApiView, DeleteCardApiView

urlpatterns = [
    path('list/', CardsListApiView.as_view()),
    path('create/', CreateCardApiView.as_view()),
    path('delete/<int:pk>', DeleteCardApiView.as_view()),
    path('category/list', CategoryListApiView.as_view()),
    path('transaction/list', TransactionListApiView.as_view()),
    path('transaction/create/', CreateTransactionApiView.as_view())
]