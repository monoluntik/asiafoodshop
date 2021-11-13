from django.contrib import admin
from .models import Order


# class OrderItemInline(admin.TabularInline):
#     model = OrderItem
#     raw_id_fields = ['product']


# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'last_name', 'email',
#                     'city', 'street', 'zip',
#                     'created', 'updated']
#     list_filter = ['paid', 'created', 'updated']
#     inlines = [OrderItemInline]

admin.site.register(Order)