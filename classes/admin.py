from django.contrib import admin
from .models import Classes


class ClassesAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'max_attending',
        'attending'
    )

    ordering = ('pk',)


admin.site.register(Classes, ClassesAdmin)
