from django.forms import ModelForm,Textarea,TextInput

from .models import Nachricht

class MessageForm(ModelForm):
    class Meta:
        model = Nachricht
        fields = ['zeitstring', 'EmailAddresse', 'Nachricht_text']
        widgets = {
            'Nachricht_text': Textarea(attrs={'cols': 60, 'rows': 2}),
            'zeitstring':  TextInput(attrs={'class': 'table'}),
            'EmailAddresse': TextInput(attrs={'readonly': 'readonly'})
        }
