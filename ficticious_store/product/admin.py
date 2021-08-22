from django.contrib import admin

# Register your models here.

from .models import Product

# admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):

	list_display: tuple = ('name', 'price', 'quantity')

admin.site.register(Product, ProductAdmin)