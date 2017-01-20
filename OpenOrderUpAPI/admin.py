from django.contrib import admin
from OpenOrderUpAPI.models import *

class WebModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(XMLFeedAPI, WebModelAdmin)
