from django.contrib import admin
from OpenOrderUpCore.models import *

class WebModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Restaurant, WebModelAdmin)
admin.site.register(PosDevice, WebModelAdmin)
admin.site.register(Schedule, WebModelAdmin)
admin.site.register(Order, WebModelAdmin)
admin.site.register(Theme, WebModelAdmin)
