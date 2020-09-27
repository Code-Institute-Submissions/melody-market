from django import forms
from .models import Text
 
class CreateInText(forms.ModelForm):

    class Meta:
        model= Text
        fields = ['advert','text','phnumber',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
                'advert': 'Advert Category',
                'text': 'Your Message',
                'phnumber': 'Phone Number',
            }
        self.fields['advert'].required = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'bullet-input'
            self.fields[field].label = False