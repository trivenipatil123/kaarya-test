from django.shortcuts import render

from core_app import constants
from core_app.models import Property


def index(request):
    properties_slider = Property.objects.filter(property_for=constants.BUY)[:3]
    properties = Property.objects.all()[:3]
    return render(request, 'core_app/index.html', {"properties_slider": properties_slider, "properties": properties})


def buy_property_view(request):
    print('Request for Buy property page received')
    properties = Property.objects.filter(property_for=constants.BUY)
    return render(request, 'core_app/buy.html', {"properties": properties})


def sell_property_view(request):
    print('Request for Buy property page received')
    return render(request, 'core_app/sell.html', {})


def rent_property_view(request):
    print('Request for Rent property page received')
    properties = Property.objects.filter(property_for=constants.RENT)
    return render(request, 'core_app/rent.html', {"properties": properties})


def all_properties_view(request):
    print('Request for all properties page received')
    return render(request, 'core_app/properties.html', {})


def contact_us_view(request):
    print('Request for contact us page received')
    return render(request, 'core_app/contact.html', {})