from django.utils.html import format_html
from django.db import models
from django.contrib import admin
import hashlib

def generate_filename1(instance, filename)-> str:
	file = instance.img1.file # It's already opened there's no need to open it
	content = file.read()
	instance.img1_checksum = hashlib.sha256(content).hexdigest()
	return 'flowers/{0}-1.{1}'.format(instance.flower_id, filename.split('.')[-1])

def generate_filename2(instance, filename)-> str:
	file = instance.img2.file # It's already opened
	content = file.read()
	instance.img2_checksum = hashlib.sha256(content).hexdigest()
	return 'flowers/{0}-2.{1}'.format(instance.flower_id, filename.split('.')[-1])

class Product(models.Model):
    flower_id = models.CharField(max_length=200,unique=True)
    # The necessary steps in order to define the fields with "" by default and make them optionnal
    # Set the default argument to ""
    # Set the argument null to False to avoid storing the fields with a null value 
    # Set the blank argument to True to make it optionnal
    identite = models.TextField(null=False, blank=True, default="", verbose_name="Identité")  
    entretien = models.TextField(null=False, blank=True, default="", verbose_name="Entretien")
    floraison = models.TextField(null=False, blank=True, default="", verbose_name="Floraison")
    remarques = models.TextField(null=False, blank=True, default="", verbose_name="Remarques")
    img1 = models.ImageField(null=False,upload_to=generate_filename1, blank=True, default="")
    img1_checksum = models.TextField(null=False, editable=False, blank=True, default="")
    img2 = models.ImageField(null=False,upload_to=generate_filename2, blank=True, default="")
    img2_checksum = models.TextField(null=False , editable=False, blank=True, default="")

   
    def __str__(self):
        return self.flower_id # this display a header in the form of the product that contains the name of the flower

class ImagePreview(admin.ModelAdmin):
    readonly_fields = ('img1_preview', 'img2_preview') # we just need to preview the two images
    
    def img1_preview(self, obj):
        return format_html('<img src="{}" width="150"/>'.format(obj.img1.url))
    
    def img2_preview(self, obj):
        return format_html('<img src="{}" width="150"/>'.format(obj.img2.url))
    
    img1_preview.short_description = 'Image 1 Preview'
    img2_preview.short_description = 'Image 2 Preview'
    list_display = ["flower_id","identite","entretien","floraison","remarques","img1","img2"]



