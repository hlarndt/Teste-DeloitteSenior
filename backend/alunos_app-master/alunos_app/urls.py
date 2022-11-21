"""alunos_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt import views as jwt_views
from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions

schema_view = get_swagger_view(title='Alunos API')
SWAGGER_SETTINGS = {
   'SECURITY_DEFINITIONS': {
      'Basic': {
            'type': 'basic'
      },
      'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
      }
   }
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('alunos.urls')),
    path('login/', jwt_views.TokenObtainPairView.as_view()),    
    path('refresh-token/', jwt_views.TokenRefreshView.as_view()),
    path('openapi/', get_schema_view(
        title="Alunos API",
        description="Alunos API",
        public=True,
        version="1.0",
        permission_classes=[permissions.AllowAny]
    ), name='openapi-schema'),
    path('swagger/', TemplateView.as_view(
        template_name='swagger.html',
        extra_context={'schema_url': 'openapi-schema'},
    
    ), name='swagger-ui'),
    path('swagger/', TemplateView.as_view(
        template_name='swagger.html',
        extra_context={'schema_url': 'openapi-schema'},
    ), name='swagger-ui'),
    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='redoc'),
]
