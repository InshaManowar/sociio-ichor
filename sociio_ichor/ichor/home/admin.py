from django.contrib import admin

# Register your models here.
from .models import BloodRequest


class BloodRequestAdmin(admin.ModelAdmin):
    
    list_display=('blood_request_id','time_stamp', 'blood_group', 'blood_type', 'units','slug',)
    list_filter = ('blood_group', 'blood_type')
    
   # prepopulated_fields = {'slug': ('name',)}  

admin.site.register(BloodRequest, BloodRequestAdmin)
