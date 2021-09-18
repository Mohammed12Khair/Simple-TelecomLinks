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
