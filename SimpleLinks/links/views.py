import enum
from json.encoder import JSONEncoder
from math import fabs
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from h11 import Data
from super_manger.models import siteAttr
from .models import site_map, links
from django.urls import reverse

from .transactions import siteaction, is_ajax


# Create your views here.
def dashboard(request):
    # file_ = open("feeds.txt", "r")
    # for i in file_:
    #     line = str(i).split(",")
    #     site_map(siteid=line[0], sitename=line[1],
    #              weight=line[4], long=line[2], lat=line[3]).save()
    return render(request, 'home/dashboard.html', {})


@permission_required('AddSite', raise_exception=True)
def add_site(request):
    siteid_ = siteAttr.objects.get(key='siteid')
    sitename_ = siteAttr.objects.get(key='sitename')
    contex = {
        'siteid_': siteid_,
        'sitename_': sitename_,
    }
    if request.method == "POST":
        error = ''
        siteid = request.POST['siteid']
        sitename = request.POST['sitename']
        longitude = request.POST['longitude']
        Latitude = request.POST['Latitude']
        site_weight = request.POST['site_weight']
        try:
            add_site_ = site_map(site_id=siteid, site_name=sitename,
                                 site_long=longitude, site_lat=Latitude, site_weight=site_weight)
            add_site_.save()
            error = 'Site ' + str(siteid) + ' added Succssfuly'
        except Exception as e:
            error = str(e)
        contex = {
            'siteid_': siteid_,
            'sitename_': sitename_,
            'error': error,
        }

    return render(request, 'sitemanger/add_site.html', contex)


def site_manger(request):
    site_map_data = site_map.objects.all().order_by('-id')
    siteid_ = siteAttr.objects.get(key='siteid')
    sitename_ = siteAttr.objects.get(key='sitename')
    contex = {
        'siteid_': siteid_,
        'sitename_': sitename_,
        'site_map_data': site_map_data,
        'title': 'Sites Manger'
    }
    if request.method == "POST":
        if request.POST['action'] == "check_site_name" and is_ajax(request):
            if site_map.objects.filter(siteid=request.POST['siteid']).exists():
                return HttpResponse('1')
            else:
                return HttpResponse('0')
        if request.POST['action'] == "site_manger_add" and is_ajax(request):
            DB = siteaction('site_manger_add', request)
            if DB.commit() is not None:
                status = {
                    'error': '1',
                    'msg': DB.commit(),
                    'TableData': DB.TableData()
                }
            else:
                status = {
                    'error': '0',
                    'msg': 'Site added success',
                    'TableData': DB.TableData()
                }
            return JsonResponse(status, safe=False)
        if request.POST['action'] == "site_manger_edit" and is_ajax(request):
            DB = siteaction('site_manger_edit', request)
            if DB.commit() is not None:
                status = {
                    'error': '1',
                    'msg': DB.commit(),
                    'TableData': DB.TableData()
                }
            else:
                status = {
                    'error': '0',
                    'msg': 'Site edit success',
                    'TableData': DB.TableData()
                }
            return JsonResponse(status, safe=False)
            # if DB.commit() is not None:
            #     contex['msg'] = DB.commit()
    return render(request, 'sitemanger/index.html', contex)


def site_manger_delete(request):
    try:
        site_map.objects.filter(id=request.POST['id']).delete()
        status = {
            'error': '0',
            'msg': 'Site removed from list'
        }
    except Exception as e:
        status = {
            'error': '1',
            'msg': 'Failed'
        }
    return JsonResponse(status, safe=False)


def maps(request):
    return render(request, 'map/index.html', {})


def map_controller(request):
    if request.method == "POST" and is_ajax(request):
        if request.POST['action'] == 'initialization_':
            initialization_data = list(
                site_map.objects.all().values('siteid', 'long', 'lat'))
            return JsonResponse(initialization_data, safe=False)
        if request.POST['action'] == 'linkManger_':

            try:
                site_data = site_map.objects.get(id=request.POST['siteid'])
                site_link = list(links.objects.filter(
                    siteA=site_data).values('siteB'))
                GetSiteBIds = links.objects.filter(siteA=site_data)
                SiteBId = []
                for i in GetSiteBIds:
                    # print("i.siteB _______")
                    SiteBId.append(i.siteB.id)
                    # print(i.siteB.id)
                    # print(i.siteB.siteid)
                    # print(i.siteB.sitename)
                    # print(i.siteB.long)
                    # print(i.siteB.lat)
                    # print(i.link_name)
                SiteBData = list(site_map.objects.filter(id__in=SiteBId).values(
                    'id', 'sitename', 'siteid', 'long', 'lat', 'status'))
                # Adding link Status
                for link in range(0, len(SiteBData)):
                    SiteBData[link]['link_name'] = links.objects.get(
                        siteB=SiteBData[link]['id']).link_name
                    # link_data=links.objects.get(siteB=SiteBData[link]['']);
                # data={
                #     'site_link':site_link,
                # }
                print("linkManger_")
                return JsonResponse(SiteBData, safe=False)
            except Exception as e:
                print("Error", e)
                pass
    return HttpResponse("asdsad")


# Links Manger
def linksManger(request, siteid):
    contex = {
        'title': 'Links Manger'
    }

    if request.method == "POST":
        site_a = request.POST['site_a']
        link_name = request.POST['link_name']
        site_b = request.POST['site_b']
        links(siteA=site_map.objects.get(siteid=site_a),
              siteB=site_map.objects.get(siteid=site_b),
              link_name=link_name
              ).save()

    try:
        site = site_map.objects.get(id=siteid)
        linksdata = links.objects.filter(siteA=siteid)
        sites_destination = site_map.objects.all()
        contex['site'] = site
        contex['linksdata'] = linksdata
        contex['siteid'] = siteid
        contex['sites_destination'] = sites_destination
    except Exception as e:
        print("Error=>" + str(e))

    return render(request, 'linksManger/index.html', contex)

# To Reload DataTable{SitesTable} with new Data


def SitesTable(request):
    if is_ajax(request):
        Links = reverse('linksManger', kwargs={'siteid': '1'})
        Edit = '<button class="btn btn-sm btn-info edit_site_btn" data-toggle="modal" data-target="#editform" row="{}"><i class="fa fa-edit"></i> EDIT</button>'
        Delete = '<button class="btn btn-sm btn-danger delete_btn" row="{}"><i class="fa fa-trash"></i> DELETE</button>'
        DataTable = list(site_map.objects.all().values(
            'id', 'sitename', 'siteid', 'long', 'lat', 'weight', 'status').order_by('-id'))
        index = 0
        for data in DataTable:
            DataTable[index]['action'] = '<div style="text-align: center;margin:1px;">'
            DataTable[index]['action'] += '<a class="btn btn-sm btn-primary edit_site_btn"  href="' + \
                reverse('linksManger', kwargs={
                        'siteid': data['id']}) + '"  ><i class="fa fa-edit"></i>LINKS</a>'
            DataTable[index]['action'] += Edit.format(data['id'])
            DataTable[index]['action'] += Delete.format(data['id'])
            DataTable[index]['action'] += "</div>"
            # DataTable[index]['action']='<div class="nav-item dropdown no-arrow "><a class="dropdown-toggle nav-link" data-toggle="dropdown" aria-expanded="true" href="#"><span class="d-none d-lg-inline mr-2 text-gray-600 small">admin</span></a>\
            #         <div class="dropdown-menu shadow dropdown-menu-right animated--grow-in " role="menu"><a class="dropdown-item" role="presentation" href="#"><i class="fas fa-user fa-sm fa-fw mr-2 text-gray-400"></i>&nbsp;Profile</a><a class="dropdown-item" role="presentation" href="#"><i class="fas fa-cogs fa-sm fa-fw mr-2 text-gray-400"></i>&nbsp;Settings</a>\
            #             <a class="dropdown-item" role="presentation" href="#"><i class="fas fa-list fa-sm fa-fw mr-2 text-gray-400"></i>&nbsp;Activity log</a>\
            #             <div class="dropdown-divider"></div><a class="dropdown-item" role="presentation" href="#"><i class="fas fa-sign-out-alt fa-sm fa-fw mr-2 text-gray-400"></i>&nbsp;Logout</a></div>\
            #     </div>'
            index += 1
        return JsonResponse(DataTable, safe=False)


def GetSite(request):
    if request.method == 'POST' and is_ajax(request):
        GetSite = site_map.objects.filter(id=request.POST['id']).values(
            'id', 'sitename', 'siteid', 'long', 'lat', 'weight', 'status')[0]
        return JsonResponse(GetSite, safe=False)
