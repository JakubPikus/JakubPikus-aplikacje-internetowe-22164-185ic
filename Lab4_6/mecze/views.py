from django.contrib.auth import get_user_model 
from rest_framework import generics, permissions, viewsets, filters

from .models import Mecz
from .permissions import IsAuthorOrReadOnly 
from .serializers import UserSerializer, MeczSerializer



class MeczList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
   

    queryset = Mecz.objects.all()
    serializer_class = MeczSerializer
   



class MeczViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Mecz.objects.all()
    serializer_class = MeczSerializer
    filter_backends = [filters.SearchFilter ,filters.OrderingFilter]
    search_fields = ['id'] 
    
    

class UserViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    

class MeczDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    

    queryset = Mecz.objects.all()
    serializer_class = MeczSerializer



class UserList(generics.ListCreateAPIView):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer




