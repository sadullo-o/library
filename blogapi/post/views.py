from rest_framework.authentication import TokenAuthentication
import requests
from .serializers import PostSerializer, UsersSerializer, TovarSerializer, KorzinaSerializer, ZakazSerializer, VideoSerializer
from django.contrib.auth import get_user_model
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .permissions import IsAuthorOrReadOnly
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import Post, Tovarlar, Korzina, Zakaz, Video
# Create your views here.


class TovarlarView(ListAPIView):
    queryset = Tovarlar.objects.all()
    serializer_class = TovarSerializer

    # --------------
    Video.objects.all().delete()
    # --------------

class VideoView(ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoViewGet(ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Video.objects.all()
    serializer_class = VideoSerializer



class KorzinaView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Korzina.objects.all()
    serializer_class = KorzinaSerializer

class KorzinaViewDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Korzina.objects.all()
    serializer_class = KorzinaSerializer



class ZakazView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Zakaz.objects.all()
    serializer_class = ZakazSerializer

# class ZakazViewDetail(RetrieveUpdateDestroyAPIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     queryset = Zakaz.objects.all()
#     serializer_class = ZakazSerializer

class PostViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # authentication_classes = (TokenAuthentication,)


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UsersSerializer



# gmail.com




# class PostList(ListCreateAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     # permission_classes = (permissions.IsAdminUser,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostDetail(RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class UserList(ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UsersSerializer
#
# class UserDetail(RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UsersSerializer