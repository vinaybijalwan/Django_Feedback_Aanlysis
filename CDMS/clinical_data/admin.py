from django.contrib import admin
from .models import patientinfo
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.
#old one
#admin.site.register(patientinfo)


class patientinfoAdmin(admin.ModelAdmin):
    list_display = ('HIN', 'patient_name', 'visit_date', 'disease', 'doctor_name')

#admin.site.register(patientinfoAdmin)


#Its for export and import data
class patientResource(resources.ModelResource):

    class Meta:
        model = patientinfo

class patientAdmin(ImportExportModelAdmin):
    resource_class = patientResource
admin.site.register(patientinfo, patientAdmin)


