import uuid
from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField()


class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length=255)
    email = models.EmailField()
    is_admin = models.BooleanField(default=False)


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    venue = models.CharField(max_length=255)
    link = models.URLField(null=True, blank=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    category = ArrayField(
        models.CharField(max_length=20,),
        size=5, blank=True,
    )
    is_free = models.BooleanField(default=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, auto_now=True)


class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Place(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
