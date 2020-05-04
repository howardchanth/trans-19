from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Visit)
admin.site.register(Location)
admin.site.register(Patient)
