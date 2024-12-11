from django.contrib import admin

# Register your models here.
from .models import Task

# Register Task model
admin.site.register(Task)
