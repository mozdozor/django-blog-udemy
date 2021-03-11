from django import forms
from blog.models import iletisimModel


class IletisimForm(forms.ModelForm):
    class Meta:
        model=iletisimModel
        fields=('isim_soyisim','email','mesaj')








#form control classının adının boostrap sitesindne öğrendik
# widgetlar ile html koduna direkt müdahale edebiliriz
#mesaj=forms.CharField(widget=forms.Textarea(attrs={
# 
#   "class":"deneme"
# }))   mesela burada textareanın clasını deneme yaptık

#       https://docs.djangoproject.com/en/3.1/ref/forms/widgets/   detaylı bilgiye buradan ulaşabilirsiniz