from django.contrib import admin
from .models import *
 

class AdvertAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
    )

class TextAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'date_created',
        'advert',
    )

admin.site.register(Advert, AdvertAdmin)
admin.site.register(Text, TextAdmin)