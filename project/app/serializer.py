from rest_framework import serializers
from .models import Quote, Event, Blogpost



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"



class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = "__all__"


class BlogpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogpost
        fields = "__all__"
