from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import doctor, cato, doctors_list


class catoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(cato, catoAdmin)


class proAdmin(admin.ModelAdmin):

    list_display = ['name', 'image', 'dept']
    list_editable = ['image', 'dept']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(doctor, proAdmin)

admin.site.register(doctors_list)