from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from blog.forms import YaziGuncelleModelForm
from blog.models import YazilarModel


@login_required(login_url="/")
def yazi_guncelle(request,slug):
    yazi=get_object_or_404(YazilarModel,slug=slug,yazar=request.user)
    form=YaziGuncelleModelForm(request.POST or None,files=request.FILES or None,instance=yazi) #instance (formdaki value görevini görmektedir)
    if form.is_valid():
        form.save()
        return redirect("detay",slug=yazi.slug)
    
    return render (request,"pages/yazi-guncelle.html",context={
        "form":form
    })