
from django.contrib import admin
from django.urls import path,include
import Apphome.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("Apphome.urls")),
]
