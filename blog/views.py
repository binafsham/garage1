from django.shortcuts import render
from .models import Cars, Features, Devos

# Create your views here.
def index(request):
    car = Cars.objects.all()
    features = Features.objects.all()
    devos = Devos.objects.all()
    context = {
        "car": car,
        "features": features,
        "devos": devos,
    }
    return render(request,'index.html', context=context)

def contact(request):
    return render(request,'contact.html', context={})




def devosdetail(request, id):
    devos = Devos.objects.get(id=id)
    context = {
        'x': devos
    }
    return render(request, 'devosdetail.html', context=context)

def featuresdetail(request, id):
    features = Features.objects.get(id=id)
    context = {
        'x': features
    }
    return render(request, 'featuresdetail.html', context=context)

def carsdetail(request, id):
    cars = Cars.objects.get(id=id)
    context = {
        'x': cars
    }
    return render(request, 'carsdetail.html', context=context)
