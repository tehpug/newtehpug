from rest_framework import viewsets

from pug_sessions.models import PugSession, Place
from pug_sessions.serializers import PlaceSerializer, PugSessionSerializer


class PlaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class SessionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PugSession.objects.all()
    serializer_class = PugSessionSerializer
