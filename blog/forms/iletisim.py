from django import forms
from blog.models import iletisimModel
from django.core.mail import send_mail

class IletisimForm(forms.ModelForm):
    class Meta:
        model=iletisimModel
        fields=('isim_soyisim','email','mesaj')

    def send_email(self,form):
        print(form.cleaned_data.get("email"))
        send_mail(
            subject="İletişim Formundan Yeni Mesajınız Var",
            message=form.cleaned_data.get("mesaj")+" "+form.cleaned_data.get("email"),
            #from_email=form.cleaned_data.get("email"),
            from_email=None,
            recipient_list=["muhammetay651@gmail.com"],
            fail_silently=False
        )






#form control classının adının boostrap sitesindne öğrendik
# widgetlar ile html koduna direkt müdahale edebiliriz
#mesaj=forms.CharField(widget=forms.Textarea(attrs={
# 
#   "class":"deneme"
# }))   mesela burada textareanın clasını deneme yaptık

#       https://docs.djangoproject.com/en/3.1/ref/forms/widgets/   detaylı bilgiye buradan ulaşabilirsiniz