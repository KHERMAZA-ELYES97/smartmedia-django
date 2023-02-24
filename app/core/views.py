from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, JsonResponse
from .models import Product
from django.core import serializers
import json
import requests
from pathlib import Path

def home(request):
    return HttpResponse('<h1>Test</h1>')

"""
def home(request,*args,**kwargs):
    return render(request,'index.html')
"""
def product_info(request):
    form = Product.objects.all()
    #import pdb; pdb.set_trace()
    #test = [p for p in form]

    output = []
    for flower_obj in form:
        new_dic = {
        "tag": flower_obj.flower_id,
        "text1": flower_obj.identite,
        "text2": flower_obj.entretien,
        "text3": flower_obj.floraison,
        "text4": flower_obj.remarques,
        "img1": flower_obj.img1.url,
        "img2": flower_obj.img2.url,
        "img1_checksum": flower_obj.img1_checksum,
        "img2_checksum": flower_obj.img2_checksum,
        }
        output.append(new_dic)
    return JsonResponse(output, safe=False) # Only accepts dicts otherwise

def contact(request):
    return HttpResponse('contact')

def blog(request):
    return HttpResponse('blog')


