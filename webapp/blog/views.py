from django.shortcuts import render
from django.views import View
from .forms import ProductForm
from .models import Product
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer
# Create your views here.
def home_view(request, *args, **kwargs ):
    scon ={}
    return render(request, 'home.html', scon) 
def base_view(request, *args, **kwargs ):
    scon ={}
    return render(request, 'ecom.html', scon)
def form_view(request):
   form =ProductForm(request.POST or None)
   if form.is_valid():
        form.save()
   form =ProductForm(request.POST)
   scon ={
   'form':form
   }
   return render(request, 'form.html', scon)
   class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

