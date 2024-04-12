from django.shortcuts import render
from rest_framework import viewsets
from . models import *
from .serializers import *

class StudentsView(viewsets.ModelViewSet):
    queryset=students.objects.all()
    serializer_class=StudentSerializers