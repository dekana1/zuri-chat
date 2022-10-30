from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from zuri_chat.serializers import BioSerializer
from zuri_chat.models import bio


class BioViewSet(viewsets.ModelViewSet):
   queryset = bio.objects.all()
   serializer_class = BioSerializer

