from django.db import models

# Create your models here.
class site_map(models.Model):
	site_id = models.CharField(max_length=1000,default='')
	site_name = models.CharField(max_length=1000,default='')
	site_long = models.CharField(max_length=1000,default='')
	site_lat = models.CharField(max_length=1000,default='')
	site_weight = models.CharField(max_length=1000,default='')
	site_status = models.CharField(max_length=1000,default='')
	site_E = models.CharField(max_length=1000,default='')
	site_Eby = models.CharField(max_length=1000,default='')

class site_links(models.Model):
	site_A= models.CharField(max_length=1000,default='')
	site_B= models.CharField(max_length=1000,default='')