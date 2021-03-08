from django.shortcuts import render

def anasayfa(request):
    context={
        "isim":"akfasdf"
    }
    return render(request,"pages/anasayfa.html",context=context)