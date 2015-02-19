from rest_framework import serializers

from projects.models import License, Project, Technology


class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
