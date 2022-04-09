from django.urls import include, path
from .views import *
urlpatterns = [
    path('', dashboard,name='home'),
    path('add_site/', add_site,name="add_site"),
    path('site_manger/', site_manger,name="SiteManger"),
    path('site_manger/SitesTable', SitesTable,name="SitesTable"),
    path('site_manger/GetSite', GetSite,name="GetSite"),
    path('site_manger_delete/', site_manger_delete,name="delete"),
    path('linksManger/<int:siteid>', linksManger,name="linksManger"),
    path('maps/', maps,name="maps"),
    path('maps/map_controller', map_controller,name="map_controller"),

]