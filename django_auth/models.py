from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class SaltExternalAuthModel(models.Model):
    user_fk = models.ForeignKey(User)
    minion_or_fn_matcher = models.CharField(max_length=600, blank=True, null=True)
    minion_fn = models.CharField(max_length=600, blank=True, null=True)

    def __unicode__(self):
        return self.minion_fn
