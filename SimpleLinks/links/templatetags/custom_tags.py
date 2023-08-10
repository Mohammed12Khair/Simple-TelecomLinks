from django import template
from links.models import *


register = template.Library()


@register.simple_tag
def getLinkStatus(SiteID):
    print(SiteID)
    print(site_map.objects.get(siteid=SiteID).status)
    return site_map.objects.get(siteid=SiteID).status