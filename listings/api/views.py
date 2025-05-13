from django.shortcuts import render
from rest_framework import generics
from .models import House
from .serializers import HouseSerializer
from rest_framework import viewsets


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer