from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from blog.forms import YaziEkleModelForm

@login_required(login_url="/")
def yazi_ekle(request):
    form=YaziEkleModelForm(request.POST or None,files=request.FILES or None)
    if form.is_valid():
        yazi=form.save(commit=False)
        yazi.yazar=request.user
        yazi.save()
        form.save_m2m() #buradaki save manytomanyfield alanının kaydı için yapıldı
        #form başarılı şekilde kaydolduktan sonra şimdi onu yönlendirmemiz gerkiyor
        return redirect('detay',slug=yazi.slug) #urls.py deki detay adındaki url ye yönlendirdik
    return render (request,"pages/yazi-ekle.html",context={
        "form":form
    })