from django.urls import path
from core_app import views as core_views

urlpatterns = [
    path('', core_views.index, name='index'),
    path('buy', core_views.buy_property_view, name='buy_property'),
    # path('sell', core_views.sell_property_view, name='sell_property'),
    path('rent', core_views.rent_property_view, name='rent_property'),
    path('properties', core_views.all_properties_view, name='all_properties'),
    path('contact_us', core_views.contact_us_view, name='contact_us'),
]