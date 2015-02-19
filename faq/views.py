from rest_framework import viewsets

from faq.models import FAQ
from faq.serializers import FAQSerializer


class FAQViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
