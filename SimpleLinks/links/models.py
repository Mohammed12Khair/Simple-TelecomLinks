from django.db import models

# Create your models here.
class site_map(models.Model):
	site_id = models.CharField(max_length=7,unique=True,blank=False)
	site_name = models.CharField(max_length=30,default='')
	site_long = models.CharField(max_length=1000,default='')
	site_lat = models.CharField(max_length=1000,default='')
	site_weight = models.CharField(max_length=1000,default='')
	site_status = models.CharField(max_length=1000,default='')
	site_E = models.CharField(max_length=1000,default='')
	site_Eby = models.CharField(max_length=1000,default='')