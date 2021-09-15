from django.contrib import admin
from .models import news
# Register your models here.
class newsAdmin(admin.ModelAdmin):
    list_display = ['heading','image']
    list_editable = ['image']
    prepopulated_fields = {'slug': ('heading',)}
admin.site.register(news, newsAdmin)


