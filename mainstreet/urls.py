from django.contrib import admin
from django.urls import path
from mainstreet.views import IndexView, InstrumentList, EquipmentList, HomeView, AboutOwner

urlpatterns = [
    path('', IndexView.as_view(template_name='base.html'), name="base"),
    # path('', HomeView.as_view(template_name='home.html'), name="home"),
    path('instrument/', InstrumentList.as_view(template_name='instrumentlist.html'), name="instruments"),
    path('equipment/', EquipmentList.as_view(template_name='equipmentlist.html'), name="equipment"),
    path('about/', AboutOwner.as_view(template_name='about.html'), name='about'),
]