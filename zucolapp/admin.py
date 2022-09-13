from django.contrib import admin
from zucolapp.models import registration
# Register your models here.

class extendmodel(admin.ModelAdmin):
    list_display = ('user','Travel_date','Phone_number')
admin.site.register(registration,extendmodel)