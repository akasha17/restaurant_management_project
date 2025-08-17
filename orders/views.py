from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def homepage(request):
    context={
        'restaurant_name':settings.RESTAURANT_NAME

    }
    return render(request, 'homepage.html',context)