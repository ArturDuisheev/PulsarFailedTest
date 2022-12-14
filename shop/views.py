import json

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PulsarProduct
from .serializers import PulsarProductSerializer


class ProductPulsarView(ListCreateAPIView):
    queryset = PulsarProduct.objects.all()
    serializer_class = PulsarProductSerializer

    def post(self, request, *args, **kwargs):
        serializer = PulsarProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(name=request.data['name'])
        return JsonResponse(serializer.data)


class ProductPulsarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = PulsarProduct.objects.all()
    serializer_class = PulsarProductSerializer
