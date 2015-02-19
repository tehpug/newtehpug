from rest_framework import serializers

from slideshows.models import Slideshow


class SlideshowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slideshow
