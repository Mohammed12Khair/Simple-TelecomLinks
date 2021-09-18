from django.urls import include, path
from .views import *
urlpatterns = [
    path('', dashboard),
    path('add_site/', add_site,name="add_site"),
    path('site_manger/', site_manger,name="add_site"),
    path('site_manger_delete/<int:id>', site_manger_delete,name="delete"),
    # path('help/', include('apps.help.urls')),
    # path('credit/', include(extra_patterns)),
]