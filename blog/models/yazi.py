from django.db import models
from autoslug import AutoSlugField
from blog.models import KategoriModel
#from django.contrib.auth.models import User  user clasında güncelleme yaptığımız için bunuda disabled yaptık
from ckeditor.fields import RichTextField
from blog.abstract_models import DateAbstractModel   #yazdığımız date abstrack clasını import ettik

class YazilarModel(DateAbstractModel):    #models.Modeli silip import ettiğimiz classı yazdık zaten o da temelinde mdoels.Model classsını içeriyor
    resim=models.ImageField(
        upload_to="yazi_resimleri",
    )
    baslik=models.CharField(max_length=50)
    icerik=RichTextField()
    
    slug=AutoSlugField(populate_from="baslik",unique=True)
    kategoriler=models.ManyToManyField(KategoriModel,related_name="yazi")
    yazar=models.ForeignKey("account.CustomUserModel",on_delete=models.CASCADE,related_name="yazilar")

    class Meta:
        verbose_name="Yazi"
        verbose_name_plural="Yazilar"
        db_table="Yazi"


    def __str__(self):
        return self.baslik