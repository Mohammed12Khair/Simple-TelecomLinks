from .models import *

class siteaction:
    def __init__(self,action,request) -> None:
        self.action=action
        self.request=request
    def commit(self):
        if self.action == "site_manger_add":
            try:
                add_site=site_map(sitename=self.request.POST['sitename'],siteid=self.request.POST['siteid'],\
                    long=self.request.POST['long'],lat=self.request.POST['lat'],weight=self.request.POST['weight'])
                add_site.save()
            except Exception as e:
                # Error code #001
                return str(e) + " #001"
        if self.action =='site_manger_edit':
            try:
                site_map.objects.filter(id=self.request.POST['id']).update(sitename=self.request.POST['sitename'],siteid=self.request.POST['siteid'],\
                    long=self.request.POST['long'],lat=self.request.POST['lat'],weight=self.request.POST['weight'])

            except Exception as e:
                return str(e) + " #002"
    def TableData(self):
        html=''
        counter=0
        Table_Data=site_map.objects.all().order_by('-id')
        for i in Table_Data:
            html+='<tr>\n'
            html+='<td>' + str(counter) + '</td>\n'
            html+='<td class="' + str(i.id) + 'siteid">' + str(i.siteid) +  '</td>\n'
            html+='<td class="' + str(i.id) + 'sitename">' + str(i.sitename) + '</td>\n'
            html+='<td class="' +str( i.id) + 'long">' + str(i.long) + '</td>\n'
            html+='<td class="' +str( i.id) + 'lat">' + str(i.lat) + '</td>\n'
            html+='<td class="' +str( i.id) + 'weight">' + str(i.weight) + '</td>\n'
            html+='<td class="' +str( i.id) + 'status">' + str(i.status) + '</td>\n'
            html+='<td style="text-align: center;">\n'
            html+='<button class="btn btn-sm btn-info edit_site_btn" data-toggle="modal" data-target="#editform" row="' + str(i.id) + '"><i class="fa fa-edit"></i> EDIT</button>\n'
            html+='<button class="btn btn-sm btn-danger delete_btn" row="' + str(i.id) + '"><i class="fa fa-trash"></i> DELETE</button>\n'
            html+='</td>\n</tr>\n'
        return html

