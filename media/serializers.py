from rest_framework import serializers

from media.models import Audio, Image, Presentation, Video


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image


class PresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentation


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
