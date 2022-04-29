from tkinter import CASCADE
from django.db import models

# Create your models here.
class site_map(models.Model):
	siteid = models.CharField(max_length=7,unique=True,blank=False)
	sitename = models.CharField(max_length=30,default='')
	long = models.CharField(max_length=1000,default='')
	lat = models.CharField(max_length=1000,default='')
	weight = models.CharField(max_length=1000,default='')
	status = models.CharField(max_length=1000,default='up')
	impact = models.CharField(max_length=1000,default='')
	impact_by = models.CharField(max_length=1000,default='')

class links(models.Model):
	siteA=models.ForeignKey(site_map,related_name="SiteA",on_delete=models.CASCADE,default='')
	siteB=models.ForeignKey(site_map,related_name="SiteB",on_delete=models.CASCADE,default='')
	link_name=models.CharField(max_length=500,default='')
