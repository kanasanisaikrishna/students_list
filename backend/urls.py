from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import  settings
from students.views import *
from rest_framework import routers

route=routers.DefaultRouter()
route.register('',StudentsView,basename='studentslist')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(route.urls)),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)