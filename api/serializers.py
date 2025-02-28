from rest_framework import serializers
from .models import Staff,Parnters,Items,Orders

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
