from django import forms
from aluno.models import *

class AlunoForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = '__all__'
