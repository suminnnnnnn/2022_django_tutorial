from django import forms
from .models import Curriculum

class CurriculumForm(forms.ModelForm):
    class Meta:
        model = Curriculum
        fields = ['name'] # id 속성은 PK 이므로 사용하지 않음
  