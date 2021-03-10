from django import forms
from blog.models import iletisimModel


class IletisimForm(forms.Form):
    email = forms.EmailField(label="E-Posta ", max_length=75)
    isim_soyisim=forms.CharField(label="İsim Soyisim ", max_length=50)
   # mesaj=forms.Textarea()   böyle yazınca gelmedi bunu widget kllanarak ypaıcaz
    mesaj=forms.CharField(label="Mesajınız ", widget=forms.Textarea)


#yukarıdaki clası aşağıdaki gibi daha basit şekilde ypabilirsin
#class IletisimForm(forms.ModelForm):
    #class Meta:
     #   model=iletisimModel
      #  fields=('isim_soyisim','email','mesaj')
   
    


#form control classının adının boostrap sitesindne öğrendik
# widgetlar ile html koduna direkt müdahale edebiliriz
#mesaj=forms.CharField(widget=forms.Textarea(attrs={
# 
#   "class":"deneme"
# }))   mesela burada textareanın clasını deneme yaptık

#       https://docs.djangoproject.com/en/3.1/ref/forms/widgets/   detaylı bilgiye buradan ulaşabilirsiniz