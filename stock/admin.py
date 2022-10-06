from django.contrib import admin


# # Register your models here.
from .models import (
    Category,
    Product,
    Firm,
    Brand,
    Transaction
)






# class CategoryAdmin(nested_admin.NestedTabularInline):
#     model=Category
# class BrandAdmin(nested_admin.NestedTabularInline):
#     model=Brand
# class ProductAdmin(nested_admin.NestedModelAdmin):
#     model=Category
#     inlines=[CategoryAdmin,BrandAdmin]


admin.site.register(Firm)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Transaction)