from .models import Users
from rest_framework import generics, viewsets,permissions       
from rest_framework.response import Response                    
from knox.models import AuthToken
from .serializers import RegisterUser,LoginSerial
izer,UserSerializer                                             

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterUser
    def post(self, request, *args ,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user= serializer.save()
        token = AuthToken.objects.create(user)                          return Response(
    {
    "user":UserSerializer(user, context= self.get_serializer_con
text()).data,
        "token":token[1]
    }
    )                                                           class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request, *args ,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user= serializer.validated_data
        token = AuthToken.objects.create(user)
        return Response(
    {
    "user":UserSerializer(user, context= self.get_serializer_con
text()).data,                                                           "token":token[1]
    }                                                               )

class UserAPI (generics.RetrieveAPIView):
    permission_classes=[
        permissions.IsAuthenticated
    ]
    serializer_class= UserSerializer                                def get_object(self):
        return self.request.user
