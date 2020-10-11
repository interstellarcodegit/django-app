from rest_framework import routers
from .api import LeadViewSet, RegisterAPI,LoginAPI, UserAPI
from django.urls import path , include 
from knox import views as knox_views
router= routers.DefaultRouter()
router.register('apis/Users', LeadViewSet, 'users' )
urlpatterns= [path('',include(router.urls)),
              path("apis/auth",include('knox.urls')),
              path('apis/auth/register' ,RegisterAPI.as_view()),
              path('apis/auth/login' ,LoginAPI.as_view()),
              path('apis/auth/user' ,UserAPI.as_view()),
              path('apis/auth/logout' ,knox_views.LogoutView.as_view(), name= 'knox_logout')
              
             ]
