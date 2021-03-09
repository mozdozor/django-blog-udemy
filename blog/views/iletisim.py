
from django.shortcuts import render
from django.http import HttpResponse


def iletisim(request):
    context={
        "key" : "başlık içerik naber"
    }
    #return HttpResponse("<h1>Merhaba</h1>")
    return render(request,"pages/iletisim.html",context=context)


#template/pages/aanasayfa.html yazmadık çünkü django ilk olarak template klasörü varmı diye balıyor eğer varsa
#içine girip pages dosyasını aramaya başlıyor