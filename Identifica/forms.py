# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from .models import Individuo

class IndividuoForm(ModelForm):

	class Meta:
		model = Individuo
        fields = ['nome' , 'alcunha', 'sexo' , 'natural' , 'foto' , 'status']

class IndvForm(forms.Form):
    foto = forms.ImageField()
    nome = forms.TextInput()
    alcunha = forms.TextInput()

