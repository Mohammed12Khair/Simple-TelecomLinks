from django.db import models

# Create your models here.       
class PermissionMaster(models.Model):        
    class Meta:
        managed = False 
        default_permissions = ()
        permissions = ( 
            ('AddSite', 'Add New Site'),  
            ('vendor_rights', 'Global vendor rights'), 
            ('any_rights', 'Global any rights'), 
        )

class siteAttr(models.Model):
    key=models.CharField(max_length=30,blank=True)
    value=models.IntegerField(blank=True,default='')