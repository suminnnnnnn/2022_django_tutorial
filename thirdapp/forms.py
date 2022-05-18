from django import forms
from .models import Owner

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['name'] # id 속성은 PK 이므로 사용하지 않음
        widgets = { # fields에 명시된 속성만 사용
            'name': forms.TextInput(
            attrs={'required': False, 'size': 10}),
        }