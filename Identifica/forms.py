# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import Individuo

class IndividuoForm(ModelForm):
	"""Usando e testandno model form"""
	class Meta:
		model = Individuo
