from django.contrib import admin
from .models import Task
# Register your models here.
class Taskadmin(admin.ModelAdmin):
     list_display=['task']
admin.site.register(Task,Taskadmin)     