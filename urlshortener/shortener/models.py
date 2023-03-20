from django.db import models

# Create your models here.


class Url(models.Model):
    # Store url to shorten
    link = models.CharField(max_length=10000)
    # Link with given uuid will be passed to og link
    uuid = models.CharField(max_length=10)