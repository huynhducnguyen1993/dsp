
from django.http.response import HttpResponseNotAllowed, HttpResponseNotFound


# Create your views here.
from django.http.request import QueryDict
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.utils.html import strip_tags
from django.utils.timezone import activate
from django.views.generic import View
from django.views import View
from django.contrib import messages


from django.http import HttpResponse
import json
from django.shortcuts import get_object_or_404
import datetime
from django.contrib.auth.models import Permission
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from permistion.models import *
from io import BytesIO 
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File

from django.core.files.base import ContentFile
# Create your views here.
class BHcasper_views(LoginRequiredMixin,View):
    def get(self,request):
        
        return render(request,"barcodecasper/index.html")

    def post(self,request):
       
        serial = request.POST.getlist('mytext[]')
        
        for  item_serial  in serial:
            
            ser = Serial_Casper(seri = item_serial,active=False) 
            ser.save()
        messages.success(request,"Lưu Barcode Casper Thành Công ")
        return redirect("quet-barcode")
class BHcasper_out_views(LoginRequiredMixin,View):
    def get(self,request):
        
        return render(request,"barcodecasper/index2.html")

    def post(self,request):
       
        serial = request.POST.getlist('mytext[]')
        
        for  item_serial  in serial:
            
            ser = Serial_Casper_out(seri = item_serial,active=False) 
            ser.save()
        messages.success(request,"Lưu Barcode Casper Thành Công ")
        return redirect("quet-barcode-out")


class Loadlistbarcode(LoginRequiredMixin,View):
    def get(self,request):
        dt = request.GET.get('date')
        barcode = Serial_Casper.objects.filter(created_at = dt).order_by('-active')
        context ={
            'barcode':barcode,
            'dt':dt
        }
        return render(request,"barcodecasper/loadbarcodecasper.html",context)

class Casper(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,"barcodecasper/casper.html")
