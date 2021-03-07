from django.db import models
from autoslug import AutoSlugField   #bizim için hazır otomatik seo oluşturan kütüphane



class KategoriModel(models.Model):
    isim=models.CharField(max_length=30,blank=False,null=False)   #blank false ismi kesin olacak demek null false isimsiz de olmayacak demek
    slug=AutoSlugField(populate_from="isim",unique=True)        #slug seo linkleri için kullanılır unique dememiz benzersiz yapar eğer aynı kategoriden 2 tane varsa
    
    class Meta:
        db_table="kategori"  #eğer databse adını biz vermezsek django kendisi otomatik bir isim oluşturacaktı
        verbose_name_plural="Kategoriler"
        verbose_name="Kategori"


    def __str__(self):
        return self.isim
    

