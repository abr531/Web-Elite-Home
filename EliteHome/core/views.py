from django.shortcuts import render


# create your views here.

def index(request):

    return render(request, 'core/index.html')


def nosotros(request):

    return render(request, 'core/nosotros.html')

