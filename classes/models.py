from django.db import models
from django.contrib.postgres.fields import ArrayField

from profiles.models import UserProfile


class Classes(models.Model):

    name = models.CharField(max_length=254)
    max_attending = models.IntegerField(default=12)
    attending = ArrayField(models.CharField(max_length=50), default=list)
    class_day = models.CharField(max_length=10, default="")
    class_time = models.CharField(max_length=15)
    user = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True,
        blank=True
        )

    def __str__(self):
        return self.name
