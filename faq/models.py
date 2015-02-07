from django.db import models
from model_utils.models import TimeStampedModel


class FAQ(TimeStampedModel):
    question = models.CharField(max_length=100)
    answer = models.TextField()

    def __unicode__(self):
        return self.question
