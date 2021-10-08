
from django.http.request import QueryDict
from django.http.response import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.views import View
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import HttpResponse,JsonResponse

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
# Create your views here.
from django.views.decorators.http import require_GET,require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

import json


class Datxe(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,"xe/dashboard.html")        