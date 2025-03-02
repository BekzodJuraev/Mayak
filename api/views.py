from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import Staffserizzers,Partnerserizzers,OrderSer,BasketSer,ItemsSer
from .models import Staff,Parnters,Items
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response

class StaffAPI(APIView):
    serializer_class=Staffserizzers
    @swagger_auto_schema(
        responses={status.HTTP_200_OK: Staffserizzers(many=True)}
    )

    def get(self,request):
        staff=Staff.objects.all()
        serializer=self.serializer_class(staff,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PartnerAPI(APIView):
    serializer_class = Partnerserizzers

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: Partnerserizzers(many=True)}
    )
    def get(self,request):
        staff=Parnters.objects.all()
        serializer=self.serializer_class(staff,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class OrderAPI(APIView):
    serializer_class = OrderSer

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: OrderSer()}
    )

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BasketAPI(APIView):
    serializer_class=BasketSer

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: BasketSer()}
    )

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemsAPI(APIView):
    serializer_class = ItemsSer

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: ItemsSer(many=True)}
    )

    def get(self,request):
        items=Items.objects.all()
        serializer=self.serializer_class(items,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

