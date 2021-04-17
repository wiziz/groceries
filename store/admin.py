from django.contrib import admin
from .models import products
from .models import Category
# Register your models here.
class AdminProduct(admin.ModelAdmin):
	list_display=['name','price','category']

class AdminCategory(admin.ModelAdmin):
	list_display=['name']


admin.site.register(products, AdminProduct)
admin.site.register(Category, AdminCategory)
