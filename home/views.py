from django.shortcuts import render

# Create your views here.
from django.conf import settings

def homepage(request):
    context={
        'restaurant_name': settings.RESTAURANT_NAME
    }
    return render(request, 'homepage.html',context)


def about_us(request):
    return render(request, 'about.html')

def custom_404_view(request, exception):
    return render(request, '404.html',status=404)