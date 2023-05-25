from django.contrib import admin

from .models import Location


class LocationAdmin(admin.ModelAdmin):
    model = Location
    date_hierarchy = "updated"
    ordering = ("-updated",)
    list_display = ("__str__", "zip_code", "updated")
    search_fields = ("city", "zip_code")


admin.site.register(Location, LocationAdmin)
