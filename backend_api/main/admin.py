from django.contrib import admin
from main import models
# Register your models here.

admin.site.register(models.Vendor)
admin.site.register(models.PoductCategory)
admin.site.register(models.Product)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'mobile']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'order_time']

class OrderItemsAdmin(admin.ModelAdmin):

    list_display = ['order', 'product']

admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderItems,  OrderItemsAdmin)