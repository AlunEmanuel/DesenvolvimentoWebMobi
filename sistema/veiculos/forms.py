from django import forms
from django.forms import ModelForm
from .models import Veiculo

class VeiculoForm(ModelForm):
    class Meta:
        widgets={
            'marca' : forms.Select(attrs={"class":"form-control "}),
            'ano':forms.NumberInput(attrs={"class":"form-control","style":"width:300px;","min":"1900","max":"2025","placeholder":"Ano entre 1980 até atualmente"}),
            'combustivel': forms.Select(attrs={"class":"form-control "}),
            "modelo":  forms.TextInput(attrs={"class":"form-control "}),
            'cor': forms.Select(attrs={"class":"form-control"}),
        }
        model = Veiculo
        fields = ['marca','ano','combustivel','modelo','cor']