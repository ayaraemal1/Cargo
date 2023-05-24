from django.contrib import admin

from .models import Car


class CarAdmin(admin.ModelAdmin):
    model = Car
    date_hierarchy = "updated"
    ordering = ("-updated",)
    list_display = ("__str__", "updated")
    search_fields = ("__str__",)


admin.site.register(Car, CarAdmin)
