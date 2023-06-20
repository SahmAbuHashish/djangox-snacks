from django.contrib import admin
from .models import Snack

# Register your models here.

class CustomSnackAdmin(admin.ModelAdmin):
    model = Snack
    list_display = ['name', 'purchaser', 'desc',]
    fieldsets= (('Owner',{'fields':('purchaser',)}),('snack info',{'fields':('name','desc',)}))

    
admin.site.register(Snack, CustomSnackAdmin)