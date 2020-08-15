from django.contrib import admin

from .models import *



@admin.register(FrontpageImage)
class FrontpageImage(admin.ModelAdmin):
    list_display = ["image"]
