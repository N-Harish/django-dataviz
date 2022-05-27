from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Customer


# Register your models here.

@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    pass
