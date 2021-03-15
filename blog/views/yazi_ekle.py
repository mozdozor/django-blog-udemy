from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from blog.forms import YaziEkleModelForm
from django.views.generic import CreateView
from blog.models import YazilarModel
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class YaziEkleCreateView(LoginRequiredMixin , CreateView):
    login_url = reverse_lazy("giris")
    template_name="pages/yazi-ekle.html"
    model=YazilarModel
    fields=("baslik","icerik","resim","kategoriler")


    def get_success_url(self):
        return reverse("detay",kwargs={
            "slug":self.object.slug
        })

    def form_valid(self,form):
        yazi=form.save(commit=False)
        yazi.yazar=self.request.user
        yazi.save()
        form.save_m2m()
        return super().form_valid(form)




"""

login_url = reverse_lazy("giris")  ile giriş yapmadan yaza eklenmesini istemiyoruz 

@login_required(login_url="/") bunu yazmamız hata veriyor viewlarda o yüzden djangonun hazır loginmixini kullandık

If we are using success_url we have to use reverse_lazy().
If we are reversing inside a function we can use reverse().


reverse() returns a string & reverse_lazy() returns an <object>


"""

#get_success_url varsa sanırsam reverse kullanılıyor onun dışında bu fonksiyon dışında normal succes de kullansan 
#reverse lazy kullanılıyor

#yukarıdaki super kavramı inheritance (kalıtım) yaptığımız CreateView clasındaki form valid fonksiyonuna ulaşmak için 
#oraya super yazmak zorundayız


"""   aşağıdaki gibide yapabilirdik ama hazir createviewi kullanmak için yukarıdaki gibi yaptık

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


    """