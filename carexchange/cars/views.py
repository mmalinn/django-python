from django.shortcuts import render
from django.http import HttpResponse
from .models import Cars, Manufacturer
# Create your views here.


def index(request):
    manufacturers = Manufacturer.objects.all()
    data = {'manufacturer': manufacturers}
    return render(request, 'base.html', data)


def manufacturer(request, id):
    manufacturer_user = Manufacturer.objects.get(pk=id)
    manufacturer_cars = Cars.objects.filter(manufacturer=manufacturer_user)
    manufacture = Manufacturer.objects.all()
    data = {'manufacturer_user': manufacturer_user,
            'manufacturer_cars': manufacturer_cars,
            'manufacture': manufacture}
    return render(request, 'manufacturer_cars.html', data)


def cars(request, id):
    cars_user = Cars.objects.get(pk=id)
    data = {'cars_user': cars_user}
    return render(request, 'car.html', data)
