from rest_framework import serializers, status
from rest_framework.response import Response

from cards.models import Card, Category, Transaction



class CardS(serializers.ModelSerializer):
    card_num = serializers.IntegerField(read_only=True)
    deadline = serializers.CharField(read_only=True)

    class Meta:
        model = Card
        fields = ['card_num', 'deadline']
class CardSerializer(serializers.ModelSerializer):
    card_num = serializers.IntegerField(write_only=True)
    deadline = serializers.CharField(write_only=True)
    class Meta:
        model = Card
        fields = ['card_num', 'deadline']

    def create(self, validated_data):
        card_num = validated_data['card_num']

        user = self.context.get("request").user
        card = Card.objects.get(card_num=card_num)
        if card.phone == user.phone:
            card_create = Card.objects.create(user=user, phone=card.phone, **validated_data)
            return card_create
        else:
            raise status.HTTP_404_NOT_FOUND('Card not found', code=status.HTTP_402_PAYMENT_REQUIRED)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TransactionS(serializers.ModelSerializer):
    from_card_id = serializers.IntegerField(read_only=True)
    to_card_num = serializers.IntegerField(read_only=True)

    class Meta:
        model = Transaction
        fields = ['from_card_id', 'to_card_num', 'quantity']
class TransActionsSerializer(serializers.ModelSerializer):
    from_card_id = serializers.IntegerField(write_only=True)
    to_card_num = serializers.IntegerField(write_only=True)
    class Meta:
        model = Transaction
        fields = ['from_card_id', 'to_card_num', 'quantity']

    def create(self, validated_data):
        quantity = validated_data['quantity']
        user = self.context['request'].user
        print(user)
        from_card_id = validated_data['from_card_id']

        try:
            card_1 = Card.objects.get(id=from_card_id, user=user, is_active=True)
        except Card.DoesNotExist:
            raise serializers.ValidationError("The 'from_card' ID is invalid or inactive.")

        to_card_num = validated_data['to_card_num']
        card_2 = Card.objects.get(card_num=to_card_num, is_active=True)

        if card_1.balance < quantity:
            raise serializers.ValidationError("Card does not have enough money", code=status.HTTP_402_PAYMENT_REQUIRED)
        card_1.balance -= quantity
        card_1.save()
        card_2.balance += quantity
        card_2.save()



        transaction = Transaction.objects.create(from_card_id=from_card_id, to_card_id=card_2.id, quantity=quantity)

        return transaction




