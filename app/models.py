from django.db import models

# Create your models here.
class GeneralInfo(models.Model):
    company_name = models.CharField(max_length=255, default="company")
    location = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    open_hours = models.CharField(max_length=100, blank=True, null=True)
    video_url = models.URLField( blank=True, null=True)
    twitter_url = models.URLField( blank=True, null=True)
    facebook_url = models.URLField( blank=True, null=True)
    instagram_url = models.URLField( blank=True, null=True)
    linkedin_url = models.URLField( blank=True, null=True)
#to set the name of the added table
    def __str__(self):
        return self.company_name