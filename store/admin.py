from django.contrib import admin
from .models import Product, Category, Favourite

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class FavouriteAdmin(admin.ModelAdmin):
    list_display = (
        'userid',
        'product_ids',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Favourite, FavouriteAdmin)
