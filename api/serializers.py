from rest_framework import serializers
from .models import Staff,Parnters,Items

class Staffserizzers(serializers.ModelSerializer):
    class Meta:
        model=Staff
        fields=['photo','status','name','description']

class Partnerserizzers(serializers.ModelSerializer):
    class Meta:
        model=Parnters
        fields=['pictures']