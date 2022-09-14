from django.contrib import admin
from .models import *

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'specialization')
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(RestaurantModel, RestaurantAdmin)

