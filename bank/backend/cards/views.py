from django.db.models import Q
from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cards.models import Card, Category, Transaction
from cards.serializers import CardSerializer, CategorySerializer, TransActionsSerializer, CardS, TransactionS


# Create your views here.

# _-_-_-_-_-_-_-CRUD CARDS _-_-_-_-_-_-_-_-_-_-
class CardsListApiView(ListAPIView):

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
            cards = Card.objects.filter(user=user)
            return cards
        else:
            return {'message': 'User not found'}

    serializer_class = CardS
    permission_classes = [IsAuthenticated]


class CreateCardApiView(CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class DeleteCardApiView(DestroyAPIView):
    def get_queryset(self):
        user = self.request.user
        card = Card.objects.get(user=user)
        card.user = None
        card.save()
        return Response({'message': 'Success!'})


# -----------------------------------------------------------------
# _-_-_-_-_-_-_-_-_-_-_-CATEGORY_-_-_-_-_-_-_-_-_-_-_-
class CategoryListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# _-_-_-_-_-_-_-_-_-_-_-_-_Transactions-_-_-_-_-_-_-_-_-
class TransactionListApiView(ListAPIView):
    serializer_class = TransactionS

    def get_queryset(self):
        card_id = self.request.query_params.get('card_id')
        from_date = self.request.query_params.get('from_date')
        to_date = self.request.query_params.get('to_date')
        only_income = self.request.query_params.get('only_income')
        print(type(only_income))
        query = Transaction.objects.filter(Q(from_card=self.request.user.id)|Q(to_card=self.request.user.id))
        if card_id is not None:
            query = query.filter(Q(from_card=card_id)|Q(to_card=card_id))
        if from_date is not None:
            query = query.filter(datetime__range=(from_date, to_date))
        if only_income is not None:
            if only_income == 'true':
                query = query.filter(to_card__user=self.request.user)
            else:
                query = query.filter(from_card__user=self.request.user)

        return query
    card_id = openapi.Parameter('card_id', openapi.IN_QUERY, description='field you want to order by',
                                         type=openapi.TYPE_STRING)
    from_date = openapi.Parameter('from_date', openapi.IN_QUERY, description='field you want to order by',
                                           type=openapi.TYPE_STRING)
    to_date = openapi.Parameter('to_date', openapi.IN_QUERY, description='field you want to order by',
                                         type=openapi.TYPE_STRING)
    only_income = openapi.Parameter('only_income', openapi.IN_QUERY, description='field you want to order by',
                                             type=openapi.TYPE_BOOLEAN)


    @swagger_auto_schema(manual_parameters=[card_id, from_date, to_date, only_income])
    def get(self, request, *args, **kwargs):
        return  super().get(request, *args, **kwargs)


class CreateTransactionApiView(CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransActionsSerializer
