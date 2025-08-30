from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializers

class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers 

# Create your views here.
