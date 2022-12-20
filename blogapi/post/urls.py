from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *
# from .views import PostList, PostDetail, UserList, UserDetail

router = SimpleRouter()

router.register('users', UserViewSet, basename='users')
router.register('posts', PostViewSet, basename='post')

urlpatterns = [
    path('tovarlar', TovarlarView.as_view()),
    path('korzina', KorzinaView.as_view()),
    path('korzina/<int:pk>', KorzinaViewDetail.as_view()),
    path('zakaz', ZakazView.as_view()),
    path('video', VideoView.as_view()),
    path('videog', VideoViewGet.as_view()),
    # path('zakaz/<int:pk>', ZakazViewDetail.as_view()),
]

urlpatterns += router.urls


# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view()),
#     path('', PostList.as_view()),
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view())
#
# ]



# number = int(input("Enter the input Range : "))
# for iter in range(2,number):
#     for i in range(2,iter):
#         if (iter%i==0):
#             break
#     else:
#         print(iter)