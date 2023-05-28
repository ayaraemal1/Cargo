from django.contrib import admin

from .models import Cargo


class CargoAdmin(admin.ModelAdmin):
    """Admin panel settings for Cargo model"""

    model = Cargo
    date_hierarchy = "updated"
    ordering = ("-updated",)
    list_display = ("__str__", "weight", "description", "updated")
    search_fields = ("description",)


admin.site.register(Cargo, CargoAdmin)
