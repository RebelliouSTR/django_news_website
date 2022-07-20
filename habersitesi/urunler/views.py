from django.shortcuts import render, get_object_or_404
from .models import Urunler
from django.http import HttpResponse

# Create your views here.

def index(request):
    urunler = Urunler.objects.all()
    return render(request, 'index.html',{"urunler":urunler})

def detay(request,id):
    habergetir = get_object_or_404(Urunler,pk=id)
    return render(request,'detay.html',{'haberdetay':habergetir})
