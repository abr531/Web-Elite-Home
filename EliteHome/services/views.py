from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Service 

from rest_framework import viewsets
from .serializers import ServiceSerializer

# Create your views here.
def casas(request):
    casas = Service.objects.all()
    return render(request, "services/casas.html",{'services':casas})



class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk']
        )
        return obj
