from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Data,DataHindi
#admin.site.register(Data)
@admin.register(Data)
class PersonAdmin(ImportExportModelAdmin):
    pass
# Register your models here.
@admin.register(DataHindi)
class PersonAdmin(ImportExportModelAdmin):
    pass