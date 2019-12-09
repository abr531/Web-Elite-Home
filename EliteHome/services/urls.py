from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from .views import casas, ServiceViewSet

router = routers.DefaultRouter()
router.register('service', ServiceViewSet)

urlpatterns = [
    
    path('casas/', casas, name='casas' ),
    url(r'^Service/$', Service.as_view(), name='service'