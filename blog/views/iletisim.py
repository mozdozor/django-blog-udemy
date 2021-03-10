
from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.forms import IletisimForm
from blog.models import iletisimModel


def iletisim(request):
    form=IletisimForm()

   # form=IletisimForm(initial={
    #    "isim_soyisim":"Muhammed Aydoğan"
     #   "email":"asd@gmail.com"
   # })
    #yukarıdaki formu bu şekildede yapabilrisn initial demek htmldeki value değeri demek



    if request.method=='POST':
        form=IletisimForm(request.POST)
        if form.is_valid():
            #eğer forms/iletisim.py dosyasındaki ikinci classı çalıştırısan aşağıdaki kodları uzun uzun yazmana gerek kalmaz
            #sadece form.save() diyip bırakırsın kendisi zaten yorum satırında aldığımız o classın içinde atamaları yapmıştık
            #form.save() dedikten sonra return kısmını aynen alıp bitiriyorsun
            iletisim=iletisimModel()
            iletisim.email=form.cleaned_data["email"]
            iletisim.isim_soyisim=form.cleaned_data["isim_soyisim"]
            iletisim.mesaj=form.cleaned_data["mesaj"]
            iletisim.save()
            return redirect("anasayfa")

    context={
        "form" : form
    }
    #return HttpResponse("<h1>Merhaba</h1>")
    return render(request,"pages/iletisim.html",context=context)


#template/pages/aanasayfa.html yazmadık çünkü django ilk olarak template klasörü varmı diye balıyor eğer varsa
#içine girip pages dosyasını aramaya başlıyor