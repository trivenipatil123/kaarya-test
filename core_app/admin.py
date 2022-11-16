from django.contrib import admin
from core_app.models import Property, PropertyImage


@admin.register(Property)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("location", "landmark", "no_of_bed", "price", "furniture_type")
    list_filter = ("location", "furniture_type", )
    search_fields = ("short_desc__startswith",)


admin.site.register(PropertyImage)