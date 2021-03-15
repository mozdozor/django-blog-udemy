from django.shortcuts import render,get_object_or_404,redirect
from blog.models import YazilarModel
from blog.forms import YorumEkleModelForm
from django.views import View
from django.contrib import messages


class DetayModel(View):
    http_method_names = ['get', 'post']
    yorum_ekle_form=YorumEkleModelForm

    def get(self,request,slug):
        yazi=get_object_or_404(YazilarModel,slug=slug)
        yorumlar=yazi.yorumlar.all()
        return render(request,"pages/detay.html",context={
            "yazi":yazi,
            "yorumlar":yorumlar,
            "yorum_ekle_form":self.yorum_ekle_form()
        })

    def post(self,request,slug):
        yazi=get_object_or_404(YazilarModel,slug=slug)
        yorum_ekle_form=self.yorum_ekle_form(request.POST)        
        if yorum_ekle_form.is_valid():
            yorum=yorum_ekle_form.save(commit=False)
            yorum.yazan=request.user
            yorum.yazı=yazi
            yorum.save()
            messages.success(request,"Yorum başarıyla eklendi")
        return redirect("detay",slug=slug)







"""                 YUKARIDAKİ İŞLEMLERİ AŞAĞIDAKİ GİBİDE YAPABİLİRİZ AMA YUKARIDAKİ İŞLEM DAHA SİSTEMATİK 

tabi bunları yaptıktan sonra init de bir url kısmında ise iki kısmı değiştirmen gerek detaymodel yazman gerek

yukarıdakinin amacı def post dediğimiz kısım mesela sayfaya post işlemi yapılırsa çalışacak eğer sayfaya get 
yapılırsa def get kısmı çalışacak 

http_method_names = ['get', 'post']   ise bu sayfada izin verdiğimiz işlemler 


ve self.yorum_ekle_form yazmazsanda hata verir  buradaki self aslında classa erişmek için pythonda bir kuraldır yazman 
gerekir




def detay(request,slug):
    yazi=get_object_or_404(YazilarModel,slug=slug)
    yorumlar=yazi.yorumlar.all()


    if request.method == 'POST':
        yorum_ekle_form=YorumEkleModelForm(data=request.POST)
        if yorum_ekle_form.is_valid():
            yorum=yorum_ekle_form.save(commit=False)
            yorum.yazan=request.user
            yorum.yazı=yazi
            yorum.save()

    yorum_ekle_form=YorumEkleModelForm()  #burada tekrar bunu yazma sebebimiz yorum yaotıktan sonra yorum tezti dolu geliyordu onu engelledik

    return render(request,"pages/detay.html",context={
        "yazi":yazi,
        "yorumlar":yorumlar,
        "yorum_ekle_form":yorum_ekle_form,
    })  


"""
