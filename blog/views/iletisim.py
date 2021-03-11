
from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.forms import IletisimForm
from blog.models import iletisimModel


def iletisim(request):
    form=IletisimForm()
    if request.method=='POST':
        form=IletisimForm(request.POST)
        if form.is_valid():         
           form.save()
           return redirect("anasayfa")

    context={
        "form" : form
    }
    return render(request,"pages/iletisim.html",context=context)


#template/pages/aanasayfa.html yazmadık çünkü django ilk olarak template klasörü varmı diye balıyor eğer varsa
#içine girip pages dosyasını aramaya başlıyor