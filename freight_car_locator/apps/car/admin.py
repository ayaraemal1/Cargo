from django.contrib import admin

from .models import Car


class CarAdmin(admin.ModelAdmin):
    model = Car
    ordering = ("-updated",)
    list_display = ("__str__", "load_capacity", "updated")
    search_fields = ("unique_number",)


admin.site.register(Car, CarAdmin)
