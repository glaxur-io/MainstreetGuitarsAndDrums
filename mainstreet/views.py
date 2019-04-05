from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View, DetailView


class IndexView(TemplateView):
    template_name = 'base.html'


class HomeView(TemplateView):
    template_name = 'home.html'


# class InstrumentList(ListView):
#     pass
#
#
# class EquipmentList(ListView):
#     pass
