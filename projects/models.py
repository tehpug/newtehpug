from django.db import models
from model_utils.models import TimeStampedModel


class License(TimeStampedModel):
    name = models.CharField(max_length=50)
    url = models.URLField()

    def __unicode__(self):
        return self.name


class Technology(TimeStampedModel):
    name = models.CharField(max_length=20)
    url = models.URLField(blank=True)

    def __unicode__(self):
        return self.name


class Project(TimeStampedModel):
    name = models.CharField(max_length=50)
    description = models.TextField()
    link = models.URLField()
    source = models.URLField()
    license = models.ForeignKey(License)
    technologies = models.ManyToManyField(Technology)
    # author = models.ManyToManyField(Member)

    def __unicode__(self):
        return self.name
