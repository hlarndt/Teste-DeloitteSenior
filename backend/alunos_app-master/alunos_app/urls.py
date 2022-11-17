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
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Alunos API')

urlpatterns = [
    path('api/', include('alunos.urls')),
    path('openapi/', get_schema_view(
        title="Alunos API",
        description="API Alunos"
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='swagger.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]
