from django.db import models
from model_utils.models import TimeStampedModel


class Slideshow(TimeStampedModel):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=140)
    link = models.URLField()
    image = models.ImageField()

    def __unicode__(self):
        return self.title
