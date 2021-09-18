from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from super_manger.models import siteAttr
from .models import site_map

from .transactions import siteaction

# Create your views here.
def dashboard(request):
    return render(request,'home/dashboard.html',{})

# Site manger
@permission_required('AddSite',raise_exception=True)
def add_site(request):
    siteid_=siteAttr.objects.get(key='siteid')
    sitename_=siteAttr.objects.get(key='sitename')
    contex={
        'siteid_':siteid_,
        'sitename_':sitename_,
    }
    if request.method == "POST":
        error=''
        siteid=request.POST['siteid']
        sitename=request.POST['sitename']
        longitude=request.POST['longitude']
        Latitude=request.POST['Latitude']
        site_weight=request.POST['site_weight']
        try:
            add_site_=site_map(site_id=siteid,site_name=sitename,site_long=longitude,site_lat=Latitude,site_weight=site_weight)
            add_site_.save()
            error='Site ' + str(siteid) + ' added Succssfuly' 
        except Exception as e:
            error=str(r)
        contex={
            'siteid_':siteid_,
            'sitename_':sitename_,
            'error':error,
            }
            
    return render(request,'sitemanger/add_site.html',contex)


def site_manger(request):
    site_map_data=site_map.objects.all()
    siteid_=siteAttr.objects.get(key='siteid')
    sitename_=siteAttr.objects.get(key='sitename')
    contex={
        'siteid_':siteid_,
        'sitename_':sitename_,
        'site_map_data':site_map_data,
    }
    if request.method == "POST":
        DB=siteaction('addsite',request)
        DB.start()
    return render(request,'sitemanger/index.html',contex)
