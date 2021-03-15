
from django.urls import path,include
from blog.views import iletisim,anasayfa,kategoriListeleme,yazilarim,DetayModel,yazi_ekle,yazi_guncelle,yazi_sil,yorum_sil
from django.views.generic import TemplateView,RedirectView



urlpatterns = [ 
    path("",anasayfa,name="anasayfa"),
    path("iletisim",iletisim,name="iletisim"),
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
    path('yazi-sil/<slug:slug>', yazi_sil , name='yazi-sil'),
    path('yazi-ekle',yazi_ekle,name='yazi_ekle'),
    path('yazi-guncelle/<slug:slug>', yazi_guncelle , name='yazi-guncelle'),
    path('yorum-sil/<int:id>', yorum_sil , name='yorum-sil'),
   
]

#yukarıdaki detay kısmındaki DetayModel.asView ksımında as view yazmamızın sebebi detayModel class based tabanlı 
#bir viewdir detay.py de kodları deiştirip class tabanlı yazmıştık yani onu belirtmemiz lazım 
# yoksa kod patlar hata verir ve hata kaynağını bulmak da zor olabilir