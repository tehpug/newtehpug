from rest_framework import viewsets

from slideshows.models import Slideshow
from slideshows.serializers import SlideshowSerializer


class SlideshowViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Slideshow.objects.all()
    serializer_class = SlideshowSerializer
