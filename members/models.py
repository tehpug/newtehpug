from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from tehpug.utils import set_upload_path


class Member(TimeStampedModel):
    user = models.OneToOneField(User)

    bio = models.TextField(max_length=200, blank=True)
    avatar = models.ImageField(upload_to=set_upload_path, blank=True)
    cv_link = models.URLField(blank=True)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return self.user.get_full_name()


class SocialSite(TimeStampedModel):
    name = models.CharField(max_length=30)
    icon = ProcessedImageField(
        upload_to=set_upload_path,
        processors=[ResizeToFill(50, 50)],
        format='JPEG',
        options={'quality': 60}
    )
    links = models.ManyToManyField(Member, through='SocialLink')

    def __unicode__(self):
        return self.name


class SocialLink(TimeStampedModel):
    site = models.ForeignKey(SocialSite)
    user = models.ForeignKey(Member)
    url = models.URLField()

    def __unicode__(self):
        return self.site.name
