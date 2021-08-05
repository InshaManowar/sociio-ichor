from django.contrib import admin

# Register your models here.
from .models import BloodRequest
from django_summernote.admin import SummernoteModelAdmin

class BloodRequestAdmin(SummernoteModelAdmin):
    
    list_display=('blood_request_id','time_stamp', 'hospital_initials', 'blood_group', 'status',)
    list_filter = ('blood_group', 'blood_type', 'time_stamp')
    summernote_fields = ('note',)
    prepopulated_fields = {'slug': ('hospital_initials',)}  

admin.site.register(BloodRequest, BloodRequestAdmin)


