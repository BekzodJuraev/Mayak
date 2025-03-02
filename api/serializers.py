from rest_framework import serializers
from .models import Staff,Parnters,Items,Orders,Basket,Basketproducts,Category

class Staffserizzers(serializers.ModelSerializer):
    class Meta:
        model=Staff
        fields=['photo','status','name','description']

class Partnerserizzers(serializers.ModelSerializer):
    class Meta:
        model=Parnters
        fields=['pictures']


class OrderSer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields=['name','phone','email','message']

class BasketproductsSer(serializers.ModelSerializer):
    items = serializers.SlugRelatedField(
        queryset=Items.objects.all(),
        slug_field='name'
    )
    class Meta:
        model=Basketproducts
        fields=['items','count']

class BasketSer(serializers.ModelSerializer):
    products=BasketproductsSer(many=True)
    class Meta:
        model=Basket
        fields=['name','phone','products']

    def create(self, validated_data):
        products = validated_data.pop('products')
        basket = Basket.objects.create(**validated_data)
        for item in products:
            add_item = item.pop('items')
            count = item.pop('count')
            Basketproducts.objects.create(basket=basket, items=add_item, count=count)
        return basket


class ItemsSer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(many=True,
        queryset=Category.objects.all(),
        slug_field='name'
    )
    class Meta:
        model=Items
        fields=['name','pictures','categories']
