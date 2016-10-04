
import os, uuid

from django.db import models


class Category(models.Model):

    title           = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Collection(models.Model):

    title           = models.CharField(max_length=32)
    featured        = models.BooleanField(default=False)
    videos          = models.ManyToManyField('Video', related_name='collections')
    publish_at      = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title


def image_upload_to(instance, filename):
    return os.path.join('images', "{0}.{1}".format(str(uuid.uuid4()), filename.split(".")[-1]))


class Video(models.Model):

    category        = models.ForeignKey(Category, related_name='content_set', null=True, blank=True)
    title           = models.CharField(max_length=100)
    description     = models.TextField()
    length          = models.CharField(max_length=24, null=True, blank=True)
    feature_image   = models.FileField(upload_to=image_upload_to)
    cover_image     = models.FileField(upload_to=image_upload_to)
    video           = models.URLField(null=True, blank=True)
    publish_at      = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

