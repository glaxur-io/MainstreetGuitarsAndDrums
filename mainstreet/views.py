from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View, DetailView
from mainstreet.models import Instruments, Equipment


class IndexView(TemplateView):
    template_name = 'base.html'


class HomeView(TemplateView):
    template_name = 'home.html'


class InstrumentList(ListView):
    template_name = 'instrumentlist.html'
    model = Instruments


class EquipmentList(ListView):
    template_name = 'equipmentlist.html'
    model = Equipment
