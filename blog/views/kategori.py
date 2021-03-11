from django.shortcuts import render,get_object_or_404
from blog.models import YazilarModel , KategoriModel   
from django.core.paginator import Paginator

def kategori(request,kategoriSlug):
   kategori=get_object_or_404(KategoriModel,slug=kategoriSlug)

   yazilar=kategori.yazi.order_by("-id")   #o kategoriye ait bütün yazıları sondan listeliyoruz burada kategorilerdeki releated name sayseinde yapıyoruz
   sayfa=request.GET.get("sayfa")
   paginator=Paginator(yazilar,10)
    #paginator yazıları sayfalar ve her sayfada iki tane yazı tutar  ve aşağıda returnun içind ebizden hangi sayfa isteniyorsa o sayfadaki yazılar gösterilir
   return render(request,"pages/kategori.html",context={
       'yazilar':paginator.get_page(sayfa),
       'kategori_isim':kategori.isim,
    })