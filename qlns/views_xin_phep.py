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

        
      
        ngaynghi = request.POST.get('ngaynghi')
        ngaylamlai = request.POST.get('ngaylamlai')
        lydo = request.POST.get('lydo')
        guiduyet = request.POST.get('guiduyet')
        lienlac_ = request.POST.get('lienlac')
        
        Xinphep.objects.create(nhanvien=nhanvien,ngaynghi=ngaynghi,ngaylamlai=ngaylamlai,lydo = lydo,lienlac = lienlac_,phongban=nhanvien.phongban,guiduyet = guiduyet)
        xinphep =Xinphep.objects.filter(nhanvien=nhanvien,huy=False).order_by('-created_at')

        context={
            'xinphep':xinphep
        }

        return render(request,'xinphep/load/xin_phep.html',context)

class Loadxinphep_auto(LoginRequiredMixin,View):
    def get(self,request):
        username = request.user
        nhanvien = Nhanvien.objects.get(username=username)
        xinphep = Xinphep.objects.filter(nhanvien=nhanvien,huy=False).order_by('-created_at')

        context={
            'xinphep':xinphep
        }
        return render(request,'xinphep/load/xin_phep.html',context)
class Viewxinphep(View):
    def get(self,request):
        id_xp = request.GET.get('id-xp')
        xinphep = Xinphep.objects.get(pk=id_xp)
        
        context={
            'xinphep':xinphep,
        }
        return render(request,'xinphep/load/view_form_xin_nghi_phep.html',context)

class Editxinphep(LoginRequiredMixin,View):
    def get(self,request):
        id_xp = request.GET.get('id')
        xinphep = Xinphep.objects.filter(pk=id_xp)
        context={

        }

class Deletexinphep(LoginRequiredMixin,View):
    def get(self,request):
        username = request.user
        nhanvien = Nhanvien.objects.get(username=username)
        xinphep = Xinphep.objects.filter(nhanvien=nhanvien,huy=False).order_by('-created_at')

        context={
            'xinphep':xinphep
        }
        return render(request,'xinphep/load/xin_phep.html',context)
    def post(self,request):
        id_xp = request.POST.get('id_xp')
        username = request.user
        nhanvien = Nhanvien.objects.get(username=username)
        xp = Xinphep.objects.get(pk=id_xp)
        if xp.nhanvien == nhanvien:
            xp.delete()
            messages.success(request,"Xóa Thành Công ")
        xinphep = Xinphep.objects.filter(nhanvien=nhanvien,huy=False).order_by('-created_at')

        context={
            'xinphep':xinphep
        }
        return render(request,'xinphep/load/xin_phep.html',context)

class Duyettruongphong(LoginRequiredMixin,View):
    def get(self,request):
        username = request.user
        nhanvien = Nhanvien.objects.get(username=username)
        xinphep = Xinphep.objects.filter(phongban=nhanvien.phongban,tp_duyet=False,huy=False).order_by('-created_at')

        context={
            'xinphep':xinphep
        }
        return render(request,'xinphep/xin_phep_cho_tp_duyet.html',context)

class Duyetsep(LoginRequiredMixin,View):
    def get(self,request):
        username = request.user
        nhanvien = Nhanvien.objects.get(username=username)
        xinphep = Xinphep.objects.filter(tp_duyet=True,huy=False).order_by('-created_at')

        context={
            'xinphep':xinphep
        }
        return render(request,'xinphep/xin_phep_cho_sep.html',context)


class Loadxinphep_auto_tp(LoginRequiredMixin,View):
    def get(self,request):
        username = request.user
        nhanvien = Nhanvien.objects.get(username=username)
        nvcv = Chucvu_Congviec.objects.get(nhanvien=nhanvien)
       
        xinphep = Xinphep.objects.filter(phongban=nhanvien.phongban,tp_duyet=False,huy=False).order_by('-created_at')

        context={
                'xinphep':xinphep
                }
           
        return render(request,'xinphep/load/xin_phep_tp.html',context)


class Loadxinphep_auto_sep(LoginRequiredMixin,View):
    def get(self,request):
        username = request.user
        nhanvien = Nhanvien.objects.get(username=username)
        nvcv = Chucvu_Congviec.objects.get(nhanvien=nhanvien)
        if nvcv.tencongviec == "SEP":

            xinphep = Xinphep.objects.filter(tp_duyet=True,sep_duyet=False,huy=False).order_by('-created_at')

            context={
                'xinphep':xinphep
                }
        else:
            return HttpResponse("___Bạn Không Đủ Quyền_____ ")

        return render(request,'xinphep/load/xin_phep_sep.html',context)


class Pheduyetxinphep_tp(LoginRequiredMixin,View):
    def get(self,request):
        username = request.user
        nhanvien = Nhanvien.objects.get(username=username)
        nvcv = Chucvu_Congviec.objects.get(nhanvien=nhanvien)
        id_xp = request.GET.get('id_xp')   
        querydict = QueryDict("", mutable=True)
        
        querydict.update({
            'tp_duyet':True
        }) 
        xp =Xinphep.objects.get(pk=id_xp)
        form = Pheduyetxptp(querydict,instance=xp)
       
        form.save()
          
        xinphep = Xinphep.objects.filter(phongban=nhanvien.phongban,tp_duyet=False,huy=False).order_by('-created_at')
        context={
                'xinphep':xinphep
                }   
        return render(request,'xinphep/load/xin_phep_tp.html',context)

class Pheduyetxinphep_sep(LoginRequiredMixin,View):
    def get(self,request):
        username = request.user
        nhanvien = Nhanvien.objects.get(username=username)
        nvcv = Chucvu_Congviec.objects.get(nhanvien=nhanvien)
        id_xp = request.GET.get('id_xp')   
        querydict = QueryDict("", mutable=True)
        querydict.update({
            'sep_duyet':True
        }) 
        xp =Xinphep.objects.get(pk=id_xp)
        form = Pheduyetxpsep(querydict,instance=xp)
       
        form.save()
        xinphep = Xinphep.objects.filter(tp_duyet=True,sep_duyet=False,huy=False).order_by('-created_at')
        context={
                'xinphep':xinphep
                }   
        return render(request,'xinphep/load/xin_phep_sep.html',context)


class loadphepdaduyet(LoginRequiredMixin,View):
    def get(self,request):
        username = request.user
        nhanvien = Nhanvien.objects.get(username=username)
        xinphep = Xinphep.objects.filter(nhanvien=nhanvien,tp_duyet=True,sep_duyet=True,huy=False).order_by('-created_at')

        context={
            'xinphep':xinphep
        }
        return render(request,'xinphep/load/xin_phep_hh.html',context)


class Xinphepdaduyet(LoginRequiredMixin,View):
    def get(self,request):
        username = request.user
        nhanvien = Nhanvien.objects.get(username=username)
        xinphep = Xinphep.objects.filter(nhanvien=nhanvien,tp_duyet=True,sep_duyet=True,huy=False).order_by('-created_at')

        context={
            'xinphep':xinphep
        }
        return render(request,'xinphep/xin_phep_da_duyet.html',context)