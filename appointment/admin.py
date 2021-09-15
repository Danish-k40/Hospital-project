from django.contrib import admin
from .models import Appointment


# Register your models here.
class appoAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']


admin.site.register(Appointment)
