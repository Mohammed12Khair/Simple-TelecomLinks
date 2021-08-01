from django.contrib import admin

# Register your models here.
from .models import *

class site_map_view(admin.ModelAdmin):
    	list_display=('id','site_id','site_name','site_long','site_lat','site_weight','site_status','site_E','site_Eby',)
class site_links_view(admin.ModelAdmin):
    	list_display=('id','site_A','site_B',)


admin.site.register(site_map,site_map_view);
admin.site.register(site_links,site_links_view);
