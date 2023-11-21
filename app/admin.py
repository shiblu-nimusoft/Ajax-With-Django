from django.contrib import admin
from  .models import Demo
# Register your models here.


class DemoModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']


admin.site.register(Demo, DemoModelAdmin)

