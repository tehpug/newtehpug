from django.db import models
from model_utils.models import TimeStampedModel


class Shortlink(TimeStampedModel):
    slug = models.CharField(max_length=50)
    url = models.URLField()
    image = models.ImageField(blank=True)

    def __unicode__(self):
        return self.slug
