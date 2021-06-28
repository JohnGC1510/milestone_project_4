from django.contrib import admin
from .models import UserProfile


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'membership_type',
    )

admin.site.register(UserProfile, ProfileAdmin)
