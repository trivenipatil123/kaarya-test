from django.db import models

from core_app.constants import PROPERTY_FOR_TYPES, PROPERTY_TYPE, FURNITURE_TYPE, BUY, NEW, UNFURNISHED, \
    PROPERTY_STATUS, OPEN, PROPERTY_FACING, TYPE_OF_OWNERSHIP, ALLOWED_FOR


class Property(models.Model):
    property_for = models.CharField(choices=PROPERTY_FOR_TYPES, default=BUY, max_length=10)
    property_type = models.CharField(choices=PROPERTY_TYPE, default=NEW, max_length=10)
    furniture_type = models.CharField(choices=FURNITURE_TYPE, default=UNFURNISHED, max_length=20)
    name = models.CharField(max_length=50, blank=True, null=True)
    short_desc = models.CharField(max_length=150)
    long_desc = models.CharField(max_length=2500, blank=True, null=True)
    location = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    address = models.CharField(max_length=150, blank=True, null=True)
    landmark = models.CharField(max_length=100, blank=True, null=True)
    no_of_bed = models.IntegerField(default=1)
    no_of_bath = models.IntegerField(default=1)
    no_of_balcony = models.IntegerField(default=0)
    carper_area = models.CharField(max_length=10, blank=True, null=True)
    builtup_area = models.CharField(max_length=10, blank=True, null=True)
    super_builtup_area = models.CharField(max_length=10, blank=True, null=True)
    no_of_floor = models.IntegerField(default=0)
    floor = models.IntegerField(default=0)
    allowed_for = models.CharField(choices=ALLOWED_FOR, max_length=20, blank=True, null=True)
    facing = models.CharField(choices=PROPERTY_FACING, max_length=20, blank=True, null=True)
    type_of_ownership = models.CharField(choices=TYPE_OF_OWNERSHIP, max_length=20, blank=True, null=True)
    age_of_construction = models.CharField(max_length=50, blank=True, null=True)
    builder = models.CharField(max_length=30, blank=True, null=True)
    rera_id = models.CharField(max_length=30, blank=True, null=True)
    lifts = models.IntegerField(default=0)
    parking = models.BooleanField(default=False)
    property_contact = models.CharField(max_length=15, blank=True, null=True)
    status = models.CharField(choices=PROPERTY_STATUS, default=OPEN, max_length=10)
    posted_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='property_image', on_delete=models.CASCADE,)
    image = models.ImageField(upload_to='static/photos')

    def __str__(self):
        return str(self.property)