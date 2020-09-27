from django.contrib import admin
from .models import *
 
class TextAdmin(admin.ModelAdmin):
    list_display = (
        'date_created',
        'advert',
        'text',
    )

admin.site.register(Advert)
admin.site.register(Text)