from django.urls import include, path
from .views import *
urlpatterns = [
    path('', login_view),
    # path('help/', include('apps.help.urls')),
    # path('credit/', include(extra_patterns)),
]