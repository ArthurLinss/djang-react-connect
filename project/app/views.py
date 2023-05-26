from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import Event, Quote
from rest_framework.response import Response
from .serializer import *
from django.http import Http404
from rest_framework import status
# Create your views here.
import json

class EventView(APIView):
    def get(self, request, format=None):
        #output = [{"employee":output.employee, "department":output.department} for output in React.objects.all()]
        #return Response(output)
        events = Event.objects.all()
        event_serializer = EventSerializer(events,many=True)
        event_data = event_serializer.data

        quotes = Quote.objects.all()
        quote_serializer = QuoteSerializer(quotes,many=True)
        quote_data = quote_serializer.data

        data = event_data + quote_data

        return Response(data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print("valid")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
