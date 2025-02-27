from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import Staffserizzers,Partnerserizzers
from .models import Staff,Parnters
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response

class StaffAPI(APIView):
    serializer_class=Staffserizzers
    @swagger_auto_schema(
        responses={status.HTTP_200_OK: Staffserizzers()}
    )

    def get(self,request):
        staff=Staff.objects.all()
        serializer=self.serializer_class(staff,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PartnerAPI(APIView):
    serializer_class = Partnerserizzers

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: Partnerserizzers()}
    )
    def get(self,request):
        staff=Parnters.objects.all()
        serializer=self.serializer_class(staff,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)