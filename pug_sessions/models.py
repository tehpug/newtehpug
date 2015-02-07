from django.db import models
from model_utils.models import TimeFramedModel, TimeStampedModel

from media.models import Image, Audio, Presentation, Video
from tehpug.utils import set_upload_path


class Place(TimeStampedModel):
    name = models.CharField(max_length=50)
    address = models.TextField()
    link_to_map = models.URLField()
    image = models.ImageField(upload_to=set_upload_path)

    def __unicode__(self):
        return self.name


class PugSession(TimeStampedModel, TimeFramedModel):
    title = models.CharField(max_length=50)
    description = models.TextField()
    place = models.ForeignKey(Place)

    presentation = models.ForeignKey(Presentation, blank=True, null=True)
    image = models.ForeignKey(Image, blank=True, null=True)
    audio = models.ForeignKey(Audio, blank=True, null=True)
    video = models.ForeignKey(Video, blank=True, null=True)

    def __unicode__(self):
        return self.title
