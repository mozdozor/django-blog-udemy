from django.contrib.auth.decorators import login_required
from blog.models import YazilarModel
from django.shortcuts import get_object_or_404,redirect
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class YaziSilDeleteView(LoginRequiredMixin,DeleteView):
    login_url=reverse_lazy("giris")
    template_name="pages/yazi-sil-onay.html"
    success_url=reverse_lazy("yazilarim")
    def get_queryset(self):
        yazi=YazilarModel.objects.filter(slug=self.kwargs["slug"],yazar=self.request.user)
        return yazi




"""   success urel başarılı işlemlerin ardından dönecek url belirtiliyor deleteviewin urlsidir
burada aslında deledeview da return ettiğimiz şey silmek istediğimiz şeydir

  yazi=get_object_or_404(YazilarModel,slug=self.kwargs["slug"],yazar=self.request.user)   yukarıdaki yazi kısmına
  bunuda yazabilridik ama hata verecektir çünkü def_queryset fonksiyonu bir query set döndürmelidir o yüzden 
  object filter ile yaptık


@login_required(login_url="/")
def yazi_sil(request,slug):
    get_object_or_404(YazilarModel,slug=slug,yazar=request.user).delete()
    return redirect("yazilarim")


"""