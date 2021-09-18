from django.http.request import QueryDict
from django.http.response import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.views import View
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NhanvienSerializer
from django.http import HttpResponse
import json
from django.shortcuts import get_object_or_404
import datetime
from django.contrib.auth.models import Permission
from django.db.models import Q
from hashlib import sha1


from rest_framework import status 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView 
from django.core.paginator import Paginator
from .models import *
from .forms import *
from cdqttb.models import *
from cdqttb.forms import *

class Form_xin_phep(LoginRequiredMixin,View):
    redirect_field_name = 'redirect_to'
    def get(self,request):
        username = request.user
        nhanvien = Nhanvien.objects.get(username=username)

        form = Formxinphep()

        context = {
            'form':form,
            'nhanvien':nhanvien,
        }
        return render(request,'xinphep/don_xin_phep.html',context)

class Loadxinphep(View):
    def get(self,request):
        username = request.user
        nhanvien = Nhanvien.objects.get(username=username)

        form = Formxinphep()
        context = {
            'form':form,
            'nhanvien':nhanvien,
        }
        return render(request,'xinphep/load/form_xin_phep.html',context)

    def post(self,request):
        username = request.user
        nhanvien = Nhanvien.objects.get(username=username)

        form = Formxinphep()

        ngaynghi = request.POST.get('ngaynghi')
        ngaylamlai = request.POST.get('ngaylamlai')
        lydo = request.POST.get('lydo')
        guiduyet = request.POST.get('guiduyet')
        Xinphep.objects.create(nhanvien=nhanvien,ngaynghi=ngaynghi,ngaylamlai=ngaylamlai,lydo = lydo,guiduyet = guiduyet)
        xinphep =Xinphep.objects.filter(Q(sep_duyet=False)|Q(tp_duye=False),nhanvien=nhanvien,huy=False)

        context={
            'xinphep':xinphep
        }
        return render(request,'xinphep/load/xin_phep.html')

        