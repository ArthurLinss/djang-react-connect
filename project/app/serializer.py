from rest_framework import serializers
from .models import React, Event


class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ["employee", "department", "date"]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
