from django.db import models

# Create your models here.

class React(models.Model):
    employee = models.CharField(max_length=30)
    department = models.CharField(max_length=200)
    date = models.CharField(max_length=30, default="", null=True, blank=True)

    def __str__(self):
        return self.employee



event_typ_choices = (
    ("Quote", "Quote"),
    ("Event", "Event"),
)

class Event(models.Model):
    date = models.CharField(max_length=200, default="")
    title = models.CharField(max_length=40, default="", blank=True)
    subtitle = models.CharField(max_length=100, default="", blank=True)
    body = models.TextField(default="", blank=True)
    typ = models.CharField(max_length=20, choices=event_typ_choices, blank=True)
    info_link = models.CharField(max_length=200, default="", blank=True)
    source_link = models.CharField(max_length=200, default="", blank=True)
    video_link = models.CharField(max_length=200, default="", blank=True)
    image = models.ImageField(null=True, blank=True)
    author = models.CharField(max_length=200, default="", blank=True)
    location = models.CharField(max_length=200, default="", blank=True)

    def __str__(self):
        return self.title
