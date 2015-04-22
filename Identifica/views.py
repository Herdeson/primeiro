# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views.generic import ListView

from .models import Individuo

# Create your views here.


def teste(request):
    return render(request,'Identifica/index.html')

class IndexView(ListView):
    model = Individuo
    template_name = 'Identifica/index.html'

    def get_queryset(self):
    	return Individuo.objects.order_by('-dataModificacao')

