from django.contrib import admin
from core.models import Product,ImagePreview

# Register your models here.
admin.site.register(Product,ImagePreview) # the two classes Product and ImagePreview are in models.py