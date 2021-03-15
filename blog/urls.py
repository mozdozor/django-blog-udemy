
from django.urls import path,include
from blog.views import IletisimFormView,anasayfa,kategoriListeleme,yazilarim,DetayModel,YaziEkleCreateView,YaziGuncelleUpdateView,YaziSilDeleteView,yorum_sil
from django.views.generic import TemplateView,RedirectView



urlpatterns = [ 
    path("",anasayfa,name="anasayfa"),
    path("iletisim",IletisimFormView.as_view(),name="iletisim"),
    path("hakkimda",TemplateView.as_view(
        template_name="pages/hakkimda.html"
    ),name="hakkimda"),
    #aşağıdaki redirectviewi yönlendirmeye yarar sadece sosyal medya hesaplarında kullanabilirisn
    path('yonlendir',RedirectView.as_view(
        url="https://www.google.com"
    ),name='yonlendir'),
    path('kategori/<slug:kategoriSlug>', kategoriListeleme.as_view() , name='kategori'),
    path('yazilarim',yazilarim,name='yazilarim'),
    path('detay/<slug:slug>', DetayModel.as_view() , name='detay'),
    path('yazi-sil/<slug:slug>', YaziSilDeleteView.as_view(), name='yazi-sil'),
    path('yazi-ekle',YaziEkleCreateView.as_view(),name='yazi_ekle'),
    path('yazi-guncelle/<slug:slug>', YaziGuncelleUpdateView.as_view(), name='yazi-guncelle'),
    path('yorum-sil/<int:id>', yorum_sil , name='yorum-sil'),
   
]

#yukarıdaki detay kısmındaki DetayModel.asView ksımında as view yazmamızın sebebi detayModel class based tabanlı 
#bir viewdir detay.py de kodları deiştirip class tabanlı yazmıştık yani onu belirtmemiz lazım 
# yoksa kod patlar hata verir ve hata kaynağını bulmak da zor olabilir