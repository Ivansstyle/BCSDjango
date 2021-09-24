from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('BCS App mainpage')
# Create your views here.
