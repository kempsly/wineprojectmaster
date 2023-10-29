from django.contrib import admin
from core.models import Product, Category, Staff, ProductImages, Service
from core.models import  ProductReview

# Register your models here.
class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['user', 'title', 'product_image', 'price', 'featured']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']


class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'staff_image', 'contact']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'featured']


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'review', 'rating']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
