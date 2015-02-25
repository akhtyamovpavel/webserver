from django.contrib import admin

# Register your models here.
import shop.models

admin.site.register(shop.models.Seller)
admin.site.register(shop.models.Good)
admin.site.register(shop.models.Customer)
