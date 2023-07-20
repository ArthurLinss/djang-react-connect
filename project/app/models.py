from django.db import models

# Create your models here.

event_typ_choices = (
    ("Quote", "Quote"),
    ("Event", "Event"),
)

class Person(models.Model):
    surname = models.CharField(max_length=20,default="",blank=True)
    forename = models.CharField(max_length=20,default="",blank=True)

    def __str__(self):
        return self.surname + ", " + forename

    @property
    def name(self):
        return self.forename + " " + self.surname

class Quote(models.Model):
    title = models.CharField(max_length=200, default="", blank=True, unique=True)
    category = models.CharField(max_length=200, default="", blank=True, null=True)
    #author = models.ForeignKey(Person, on_delete=models.CASCADE)
    author = models.CharField(max_length=30, default="", blank=True)
    text = models.TextField(default="")
    helpText = models.TextField(default="", blank=True)
    date = models.CharField(max_length=20, default="", blank=True)
    context = models.TextField(default="", blank=True)
    typ = models.CharField(max_length=20, choices=event_typ_choices, blank=True, default="Quote")
    sources_link = models.TextField(default="", blank=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=200, default="", blank=True)
    url =  models.URLField(max_length=200)

    def __str__(self):
        return self.title

class Location(models.Model):
    name = models.CharField(max_length=200,default="",blank=True)
    country = models.CharField(max_length=200, default="", blank=True)

    def __str__(self):
        return self.name





class Event(models.Model):
    date = models.CharField(max_length=200, default="")
    category = models.CharField(max_length=200, default="", blank=True, null=True)
    title = models.CharField(max_length=40, default="", blank=True, unique=True)
    subtitle = models.CharField(max_length=100, default="", blank=True)
    text = models.TextField(default="", blank=True)
    typ = models.CharField(max_length=20, choices=event_typ_choices, blank=True, default="Event")
    info_link = models.CharField(max_length=200, default="", blank=True)
    sources_link = models.TextField(default="", blank=True)
    video_link = models.CharField(max_length=200, default="", blank=True)
    video_link2 = models.CharField(max_length=200, default="", blank=True)
    image = models.ImageField(null=True, blank=True)
    author = models.CharField(max_length=200, default="", blank=True)
    location = models.CharField(max_length=200, default="", blank=True)

    def __str__(self):
        return self.title


    @property
    def date_string(self):
        """
        if date is datetimefield, make some transformation here
        """
        return self.date




CV_Choices = (
    ("", ""),
    ("WE","Work Experience"),
    ("Ed", "Education"),
)



class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, default="")
    phone = models.CharField(max_length=200, default="")
    birth = models.DateTimeField(null=True, blank=True)
    location = models.TextField()

class CVItem(models.Model):
    #title = models.CharField(max_length=200, unique=True)
    date1 = models.DateTimeField(null=True, blank=True)
    date2 = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=200, default="")
    position = models.CharField(max_length=200, default="")
    position_detail = models.TextField(default="")
    description = models.TextField(default="")
    typ = models.CharField(default="", choices=CV_Choices, max_length=200)
    source_list = models.TextField()
    source_to_show = models.CharField(default="", max_length=200)


    def __str__(self):
        return self.position + " in " + self.location


class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default="", blank=True)
    text = models.TextField()
