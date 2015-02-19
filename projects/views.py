from rest_framework import viewsets

from projects.models import License, Project, Technology
from projects.serializers import LicenseSerializer, ProjectSerializer, TechnologySerializer


class LicenseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TechnologyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
