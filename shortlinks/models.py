from django.db import models
from model_utils.models import TimeStampedModel
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from tehpug.utils import set_upload_path


class Shortlink(TimeStampedModel):
    slug = models.CharField(max_length=50)
    url = models.URLField()
    image = ProcessedImageField(
        upload_to=set_upload_path,
        processors=[ResizeToFill(100, 50)],
        format='JPEG',
        options={'quality': 60},
        blank=True
    )

    def __unicode__(self):
        return self.slug
