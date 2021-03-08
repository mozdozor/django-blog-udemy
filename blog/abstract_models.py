from django.db import models


#böyle bir model oluşturma sebebi kod tekrarına düşmemek için örneğin oluşturulma tarihi
# ve düzenlenme tarihi yazi ve yorum kısmında ortak olduğu için bunu bir soyut class yapıcaz

class DateAbstractModel(models.Model):
    olusturulma_tarihi=models.DateTimeField(auto_now_add=True)
    duzenlenme_tarihi=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

    