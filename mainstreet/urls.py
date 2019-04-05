from django.contrib import admin
from django.urls import path
from mainstreet.views import IndexView, HomeView

urlpatterns = [
    path('', IndexView.as_view(template_name='base.html'), name="base"),
    # path('', HomeView.as_view(template_name='home.html'), name="home"),
]