from django.shortcuts import render
from django.core.paginator import Paginator
from core_app import constants
from core_app.models import Property


def index(request):
    properties_slider = Property.objects.filter(property_for=constants.BUY)[:3]
    properties = Property.objects.all()[:3]
    return render(request, 'core_app/index.html', {"properties_slider": properties_slider, "properties": properties})


def buy_property_view(request):
    print('Request for Buy property page received')
    properties = Property.objects.filter(property_for=constants.BUY)
    paginator = Paginator(properties, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core_app/buy.html', {"properties": properties, "page_obj": page_obj,
                                                 "no_of_pages": range(1, paginator.num_pages+1)})


def sell_property_view(request):
    print('Request for Buy property page received')
    return render(request, 'core_app/sell.html', {})


def rent_property_view(request):
    print('Request for Rent property page received')
    properties = Property.objects.filter(property_for=constants.RENT)
    paginator = Paginator(properties, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core_app/rent.html', {"properties": properties, "page_obj": page_obj,
                                                  "no_of_pages": range(1, paginator.num_pages+1)})


def all_properties_view(request):
    print('Request for all properties page received')
    return render(request, 'core_app/properties.html', {})


def contact_us_view(request):
    print('Request for contact us page received')
    return render(request, 'core_app/contact.html', {})