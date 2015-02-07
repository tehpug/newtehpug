from django.db import models
from model_utils.models import TimeStampedModel

from tehpug.utils import set_upload_path


class Slideshow(TimeStampedModel):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=140)
    link = models.URLField()
    image = models.ImageField(upload_to=set_upload_path)

    def __unicode__(self):
        return self.title
