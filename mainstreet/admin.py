from django.contrib import admin
from .models import Instruments, Equipment


admin.site.register([Instruments, Equipment])
