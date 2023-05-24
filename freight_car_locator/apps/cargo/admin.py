from django.contrib import admin

from .models import Cargo


class CargoAdmin(admin.ModelAdmin):
    model = Cargo
    date_hierarchy = "updated"
    ordering = ("-updated",)
    list_display = ("__str__", "updated")
    search_fields = ("__str__",)


admin.site.register(Cargo, CargoAdmin)
