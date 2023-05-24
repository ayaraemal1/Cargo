from django.contrib import admin

from .models import Location


class LocationAdmin(admin.ModelAdmin):
    model = Location
    date_hierarchy = "updated"
    ordering = ("-updated",)
    list_display = ("__str__", "updated")
    search_fields = ("__str__",)


admin.site.register(Location, LocationAdmin)
