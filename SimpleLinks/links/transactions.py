from .models import *

class siteaction:
    def __init__(self,action,request) -> None:
        self.action=action
        self.request=request
    def start(self):
        if self.action == "addsite":
            print(self.request.POST['sitename'])