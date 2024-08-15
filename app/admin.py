from django.contrib import admin
from app.models import GeneralInfo
# Register your models here.

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display=[ #display these specefic col
        'company_name',
        'location', 'phone',
        'open_hours'
    ]
    # set fiel to disable update :
    readonly_fields = ['email']