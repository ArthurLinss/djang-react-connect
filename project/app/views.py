from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import *
from rest_framework.response import Response
from .serializer import *
from django.http import Http404
from rest_framework import status
# Create your views here.

class EventView(APIView):
    def get(self, request, format=None):
        #output = [{"employee":output.employee, "department":output.department} for output in React.objects.all()]
        #return Response(output)
        events = Event.objects.all()
        serializer = EventSerializer(events,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print("valid")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
