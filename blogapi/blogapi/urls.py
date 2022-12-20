"""blogapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
# from rest_framework.schemas import get_schema_view
from .settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf.urls.static import static


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

schema_view = get_schema_view(
    openapi.Info(
        title="Blog Api",
        description="Nimadir nimadir",
        default_version="v1",
        contact=openapi.Contact(email="sadullochilov@gmail.com"),
        # terms_of_service="https://...."
        license=openapi.License(name="Blog api loyiha litsenziyasi")

    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('post.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration', include('dj_rest_auth.registration.urls')),
    path('api/allauth', include('allauth.urls')),
    # path('openapi', get_schema_view(
    #     title="Blog Api",
    #     description="Drf ni organish uchun yaratilgan api",
    #     version='1.1.0',
    # ), name="openapi-schema"),
    path('api/v1/auth', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),


    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0
    ), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0
    ), name='schema-redoc'),



]


if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)


# Oddiy token yordamida
# JWT token