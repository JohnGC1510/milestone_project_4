from django.contrib import admin
from .models import Classes


class ClassesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        #'max_attending',
        #'user'
    )


admin.site.register(Classes, ClassesAdmin)
