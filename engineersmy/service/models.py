from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField()


class Person(models.Model):
    name = models.TextField()
    email = models.EmailField()
    is_admin = models.BooleanField(default=False)


class Event(models.Model):
    name = models.CharField()
    description = models.TextField(null=True, blank=True)
    venue = models.CharField()
    link = models.URLField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    category = models.TextField()
    is_free = models.BooleanField(default=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True)


class Video(models.Model):
    pass


class Place(models.Model):
    pass
