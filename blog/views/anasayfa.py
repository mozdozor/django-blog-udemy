from django.shortcuts import render
from blog.models import YazilarModel    
from django.core.paginator import Paginator
from django.db.models import Q

def anasayfa(request):
   sorgu=request.GET.get('sorgu')
   yazilar=YazilarModel.objects.order_by('-id') 
   sayfa=request.GET.get("sayfa")
   paginator=Paginator(yazilar,10)
   return render(request,"pages/anasayfa.html",context={
       'yazilar':paginator.get_page(sayfa)
   })


   #distinc() fonksiyonu ile tekrar edenlerden sadece bir tane alıyoruz