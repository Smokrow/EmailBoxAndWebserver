# -*- coding: utf-8 -*-
from django.forms import ModelForm,Textarea,TextInput,ValidationError,Widget,NumberInput

from .models import Nachricht,Addresse_Predef

class MessageForm(ModelForm):
    class Meta:
        model = Nachricht
        fields = ['zeitstring', 'EmailAddresse', 'Nachricht_text']
        widgets = {
            'Nachricht_text': Textarea(attrs={'cols': 60, 'rows': 2}),
            'zeitstring':  TextInput(attrs={'class': 'table'}),
            'EmailAddresse': TextInput(attrs={'readonly': 'readonly'})
        }
class Addresse_Predef_Form(ModelForm):
    class Meta:
        model = Addresse_Predef
        fields = ['EmailAddresse', 'Color_R', 'Color_G','Color_B']

    # def clean_EmailAddresse(self):
    #     current_mail=str(self.cleaned_data.get('EmailAddresse'))
    #     mail = Addresse_Predef.objects.get(current_mail)
    #     if(mail!=None):
    #         raise ValidationError("Diese Emailaddresse wurde bereits benutzt")
    #     return current_mail

    # widgets = {
    #     'Color_R': NumberInput(attrs={'cols': 45, 'rows': 5}, label=''),
    # }


    def clean_Color_R(self):
        value = self.cleaned_data.get('Color_R')
        if (value > 255):
            return 255
        if (value < 0):
            return 0
        return value
    def clean_Color_B(self):
        value=self.cleaned_data.get('Color_B')
        if(value>255):
            return 255
        if (value< 0):
            return 0
        return value

    def clean_Color_G(self):
        value = self.cleaned_data.get('Color_G')
        if (value > 255):
            return 255
        if (value < 0):
            return 0
        return value
