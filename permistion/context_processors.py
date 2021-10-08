from django.db.models.expressions import F
from django.http import request
from django.http.response import HttpResponse

from .models import Permistions
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

def qlns_khachhanglon(request):
    if request.user.is_authenticated:
        users_xem = Permistions.objects.values_list('username').filter(chucnangapp="qlns_khachhanglon_xem")
        users_sua = Permistions.objects.values_list('username').filter(chucnangapp="qlns_khachhanglon_sua")
        
        if (request.user.pk,) in users_xem :#in qlns_khachhanglon_xem_.username
            qlns_khachhanglon_xem =True
        else:
            qlns_khachhanglon_xem = False
        if (request.user.pk,) in users_sua :#in qlns_khachhanglon_sua_.username
            qlns_khachhanglon_sua =True
        else:
            qlns_khachhanglon_sua =False

        context ={
            "xem":qlns_khachhanglon_xem,
            "sua":qlns_khachhanglon_sua,
            'user':request.user,
        }   
        return {'qlns_khachhanglon':context}

    else:
        context ={
            "xem":False,
            "sua":False,
            
        }   
        return {'qlns_khachhanglon':context}

def qlns_nhanvien(request):
    if request.user.is_authenticated:
        users_xem = Permistions.objects.values_list('username').filter(chucnangapp="qlns_nhanvien_xem")
        users_sua = Permistions.objects.values_list('username').filter(chucnangapp="qlns_nhanvien_sua")
        
        if (request.user.pk,) in users_xem :
            qlns_nhanvien_xem = True
        else:
            qlns_nhanvien_xem = False
        if (request.user.pk,) in users_sua :
            qlns_nhanvien_sua = True
        else:
            qlns_nhanvien_sua = False

        context ={
            'xem':qlns_nhanvien_xem,
            'sua':qlns_nhanvien_sua,

        }
        return {'qlns_nhanvien':context}
    else:
        context ={
            'xem':False,
            'sua':False

        }
        return {'qlns_nhanvien':context}

def qlns_xinphep(request):
    if request.user.is_authenticated:
        users_xem = Permistions.objects.values_list('username').filter(chucnangapp="qlns_xinphep_xem")
        users_sua = Permistions.objects.values_list('username').filter(chucnangapp="qlns_xinphep_sua")
        
        if (request.user.pk,) in users_xem :
            qlns_xinphep_xem = True
        else:
            qlns_xinphep_xem = False
        if (request.user.pk,) in users_sua :
            qlns_xinphep_sua = True
        else:
            qlns_xinphep_sua = False

        context ={
            'xem':qlns_xinphep_xem,
            'sua':qlns_xinphep_sua,

        }
        return {'qlns_xinphep':context}
    else:
        context ={
            'xem':False,
            'sua':False

        }
        return {'qlns_xinphep':context}

def qlns_dexuat(request):
    if request.user.is_authenticated:
        users_xem = Permistions.objects.values_list('username').filter(chucnangapp="qlns_dexuat_xem")
        users_sua = Permistions.objects.values_list('username').filter(chucnangapp="qlns_dexuat_sua")
        
        if (request.user.pk,) in users_xem :
            qlns_dexuat_xem = True
        else:
            qlns_dexuat_xem = False
        if (request.user.pk,) in users_sua :
            qlns_dexuat_sua = True
        else:
            qlns_dexuat_sua = False

        context ={
            'xem':qlns_dexuat_xem,
            'sua':qlns_dexuat_sua,

        }
        return {'qlns_dexuat':context}
    else:
        context ={
            'xem':False,
            'sua':False

        }
        return {'qlns_dexuat':context}


def qlns_giaichi(request):
    if request.user.is_authenticated:
        users_xem = Permistions.objects.values_list('username').filter(chucnangapp="qlns_giaichi_xem")
        users_sua = Permistions.objects.values_list('username').filter(chucnangapp="qlns_giaichi_sua")
        
        if (request.user.pk,) in users_xem :
            qlns_giaichi_xem = True
        else:
            qlns_giaichi_xem = False
        if (request.user.pk,) in users_sua :
            qlns_giaichi_sua = True
        else:
            qlns_giaichi_sua = False

        context ={
            'xem':qlns_giaichi_xem,
            'sua':qlns_giaichi_sua,

        }
        return {'qlns_giaichi':context}
    else:
        context ={
            'xem':False,
            'sua':False

        }
        return {'qlns_giaichi':context}
def athuvien_thuvien(request):
    if request.user.is_authenticated:
        users_sua = Permistions.objects.values_list('username').filter(chucnangapp="athuvien_thuvien_sua")
        users_xem = Permistions.objects.values_list('username').filter(chucnangapp="athuvien_thuvien_xem")
        
        if (request.user.pk,) in users_xem :
            athuvien_thuvien_xem = True
        else:
            athuvien_thuvien_xem = False
        if (request.user.pk,) in users_sua :
            athuvien_thuvien_sua = True
        else:
            athuvien_thuvien_sua = False

        context ={
            'xem':athuvien_thuvien_xem,
            'sua':athuvien_thuvien_sua,

        }
        return {'athuvien_thuvien':context}
    else:
        context ={
            'xem':False,
            'sua':False

        }
        return {'athuvien_thuvien':context}

def bhcasper(request):
    if request.user.is_authenticated:
        users_xem = Permistions.objects.values_list('username').filter(chucnangapp="bhcasper_xem")
        
        if (request.user.pk,) in users_xem :
            bhcasper_xem = True
        else:
            bhcasper_xem = False
        context ={
            'xem':bhcasper_xem,
        }
        return {'bhcasper':context}
    else:
        context ={
            'xem':False,
        }
        return {'bhcasper':context}