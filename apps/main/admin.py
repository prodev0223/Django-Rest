from django.contrib import admin

# Register your models here.
from apps.main.models import Invoice


class InvoiceAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Invoice._meta.fields
    ]

 
admin.site.register(Invoice, InvoiceAdmin)
