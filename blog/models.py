from django.db import models
from django.utils.timezone import now


class Blog(models.Model):
    url = models.CharField(default="http://google.com", max_length=100)
    title = models.CharField(default="my title", max_length=100)
    category = models.IntegerField(default=1)
    date = models.DateTimeField(default=now)
    publish = models.BooleanField(default=True)
    draft = models.BooleanField(default=True)

