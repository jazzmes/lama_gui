from django.http.response import HttpResponse
from django.shortcuts import render

def home(request):
    resp = '<html><title>LAMA</title></html>'
    return HttpResponse(resp)