from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display=['telefono', 'documento','numero_doc','departamento','provincia','distrito','zona_horaria']


admin.site.register(Profile, ProfileAdmin)

