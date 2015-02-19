from rest_framework import serializers

from members.models import Member, SocialLink, SocialSite


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink


class SocialSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialSite
