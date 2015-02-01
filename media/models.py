from django.db import models
from django.core.exceptions import ValidationError
from model_utils.models import TimeStampedModel
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from tehpug.utils import set_upload_path


class MediaBase(TimeStampedModel):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        abstract = True
        # ordering = ['-created']  # sort happens in view, better to not do it here


class Image(MediaBase):
    type = models.CharField(default='image', editable=False, max_length=15)
    image = models.ImageField(upload_to=set_upload_path)


class Audio(MediaBase):
    type = models.CharField(default='audio', editable=False, max_length=15)
    link = models.URLField()


class Presentation(MediaBase):
    type = models.CharField(default='presentation', editable=False, max_length=15)
    link = models.URLField()
    preview = ProcessedImageField(
        upload_to=set_upload_path,
        processors=[ResizeToFill(100, 50)],
        format='JPEG',
        options={'quality': 60}
    )


class Video(MediaBase):
    type = models.CharField(default='video', editable=False, max_length=15)
    preview = ProcessedImageField(
        upload_to=set_upload_path,
        processors=[ResizeToFill(100, 50)],
        format='JPEG',
        options={'quality': 60}
    )
    direct_link = models.URLField(blank=True)
    youtube_link = models.URLField(blank=True)
    aparat_link = models.URLField(blank=True)

    def clean(self):
        if not (self.direct_link or self.youtube_link or self.aparat_link):
            raise ValidationError('At least of the links should be present')
