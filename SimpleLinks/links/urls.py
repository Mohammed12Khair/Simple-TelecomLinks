from django.urls import include, path
from .views import *
urlpatterns = [
    path('', dashboard,name='home'),
    path('add_site/', add_site,name="add_site"),
    path('site_manger/', site_manger,name="SiteManger"),
    path('site_manger_delete/', site_manger_delete,name="delete"),
    path('maps/', maps,name="maps"),
    path('maps/initialization_', initialization_,name="initialization_"),

]