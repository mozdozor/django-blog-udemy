from django.shortcuts import render,redirect
from blog.forms import IletisimForm
from blog.models import iletisimModel
from django.views.generic import FormView


class IletisimFormView(FormView):
    template_name="pages/iletisim.html"
    form_class=IletisimForm

    success_url="/iletisim/email-gonderildi"

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
    





"""    aşağıdaki gibide yapabilirsin ama biz view kullanmak istediğimiz için yukarıdaki gibi yaptık bu arada 
return super kısmında return redirect self.success_url ile de yazabilrsin ama superli kullanım daha hoş ve sistematik 
duruyor


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

"""