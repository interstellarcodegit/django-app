from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from infoApi.views import *
from infoApi.api import *
from firstApi.api import *
from rest_framework import routers
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('firstApi.urls')),
    path('apis/', include('infoApi.urls')),
    
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

