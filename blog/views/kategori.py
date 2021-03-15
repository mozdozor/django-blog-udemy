from django.shortcuts import render,get_object_or_404
from blog.models import YazilarModel , KategoriModel   
from django.core.paginator import Paginator
from django.views.generic import ListView




class kategoriListeleme(ListView):
   template_name="pages/kategori.html"
   context_object_name="yazilar"
   paginate_by=2

   def get_queryset(self):
      kategori=get_object_or_404(KategoriModel,slug=self.kwargs["kategoriSlug"]) 
      return kategori.yazi.all().order_by("-id")





"""   aşağıdaki gibide yapabiliriz ama biz yukarıdaki gibi yaptık listview yapısını kullandık




def kategori(request,kategoriSlug):
   kategori=get_object_or_404(KategoriModel,slug=kategoriSlug)

   yazilar=kategori.yazi.order_by("-id")   #o kategoriye ait bütün yazıları sondan listeliyoruz burada kategorilerdeki releated name sayseinde yapıyoruz
   sayfa=request.GET.get("sayfa")
   paginator=Paginator(yazilar,2)
    #paginator yazıları sayfalar ve her sayfada iki tane yazı tutar  ve aşağıda returnun içind ebizden hangi sayfa isteniyorsa o sayfadaki yazılar gösterilir
   return render(request,"pages/kategori.html",context={
       'yazilar':paginator.get_page(sayfa),
       'kategori_isim':kategori.isim,
    })


    """