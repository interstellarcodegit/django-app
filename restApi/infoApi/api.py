from .models import Updates
from rest_framework import viewsets, permissions
from .serializers import UpdateSerializer
class UpdatesViewSet(viewsets.ModelViewSet):
    queryset= Updates.objects.all()
    permission_classes=[
      permissions.IsAuthenticated
    
    ]
    serializer_class=UpdateSerializer
   