from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from .serializers import RootSerializers
from .models import Root

class RootListCreateAPIView(viewsets.ModelViewSet):
    queryset = Root.objects.all()
    serializer_class = RootSerializers
