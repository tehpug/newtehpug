from django.db import models
from model_utils.models import TimeFramedModel, TimeStampedModel


class Place(TimeStampedModel):
    name = models.CharField(max_length=50)
    address = models.TextField()
    link_to_map = models.URLField()
    image = models.ImageField()

    def __unicode__(self):
        return self.name


class PugSession(TimeStampedModel, TimeFramedModel):
    title = models.CharField(max_length=50)
    description = models.TextField()
    place = models.ForeignKey(Place)

    def __unicode__(self):
        return self.title