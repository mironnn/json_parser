from django.db import models

# Create your models here.

class Region(models.Model):
    name=models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

class City(models.Model):
    name=models.CharField(max_length=20)
    region_id=models.ForeignKey(Region)
    area=models.FloatField(max_length=4, null=True, blank=True, default=None)
    def __unicode__(self):
        return self.name