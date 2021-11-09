from django.contrib import admin
from .models import course, message, teachers
# Register your models here.


class courseAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'is_activated',
        'seats_remaining'
    ]


admin.site.register(course, courseAdmin)
admin.site.register(message)
admin.site.register(teachers)
