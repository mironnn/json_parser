from django.contrib import admin

# Register your models here.

from json_app.models import Region, City

admin.site.register(Region)
admin.site.register(City)