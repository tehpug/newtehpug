from rest_framework import viewsets

from media.models import Audio, Image, Presentation, Video
from media.serializers import AudioSerializer, ImageSerializer, PresentationSerializer, VideoSerializer


class AudioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer


class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class PresentationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Presentation.objects.all()
    serializer_class = PresentationSerializer


class VideoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
