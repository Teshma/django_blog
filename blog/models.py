from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

##  CV sections (maybe display cv as a page showing all the sections like the post_list page)
class CV(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default="My CV")
    first_section = models.CharField(max_length=200, default="Personal Profile", blank=True)
    first_section_text = models.TextField(blank=True)
    second_section = models.CharField(max_length=200, default="Education", blank=True)
    second_section_text = models.TextField(blank=True)
    third_section = models.CharField(max_length=200, default="Technical Skills", blank=True)
    third_section_text = models.TextField(blank=True)
    fourth_section = models.CharField(max_length=200, default="Key Skills", blank=True)
    fourth_section_text = models.TextField(blank=True)
    fifth_section = models.CharField(max_length=200, default="Experience", blank=True)
    fifth_section_text = models.TextField(blank=True)
    sixth_section = models.CharField(max_length=200, default="Projects", blank=True)
    sixth_section_text = models.TextField(blank=True)
    seventh_section = models.CharField(max_length=200, default="Interest/Hobbies", blank=True)
    seventh_section_text = models.TextField(blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title