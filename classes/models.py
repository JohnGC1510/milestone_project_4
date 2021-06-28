from django.db import models
from django.contrib.postgres.fields import ArrayField


class Classes(models.Model):

    name = models.CharField(max_length=254)
    max_attending = models.IntegerField(default=12)
    attending = ArrayField(models.CharField(max_length=50), default=list)
    class_day = models.CharField(max_length=10, default="")
    class_time = models.CharField(max_length=15)

    def __str__(self):
        return self.name
