from django.contrib import admin

# Register your models here.
from .models import BloodRequest, DonorRequest
# from django_summernote.admin import SummernoteModelAdmin

class BloodRequestAdmin(admin.ModelAdmin):
    
    list_display=('blood_request_id','time_stamp', 'hospital_initials', 'blood_group', 'status',)
    list_filter = ('blood_group', 'blood_type', 'time_stamp')
    # summernote_fields = ('note',)
    prepopulated_fields = {'slug': ('hospital_initials',)}  

admin.site.register(BloodRequest, BloodRequestAdmin)


class DonorRequestAdmin(admin.ModelAdmin):
    list_display=('full_name', 'phone','city' ,'blood_group')
    list_filter=('blood_group','city', 'state', )
    formfield_overrides = {
        DonorRequest.date_of_birth: {'input_formats': ('%d/%m/%Y',)},
    }
    search_fields=('blood_group', 'city','state', 'pin_code', 'full_name')
    
admin.site.register(DonorRequest, DonorRequestAdmin)
    