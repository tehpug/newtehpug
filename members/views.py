from rest_framework import viewsets

from members.models import Member, SocialLink, SocialSite
from members.serializers import MemberSerializer, SocialLinkSerializer, SocialSiteSerializer


class MemberViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class SocialLinkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer


class SocialSiteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SocialSite.objects.all()
    serializer_class = SocialSiteSerializer
