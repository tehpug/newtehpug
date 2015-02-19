from rest_framework import serializers

from pug_sessions.models import PugSession, Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place


class PugSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PugSession
