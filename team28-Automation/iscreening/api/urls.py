from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.conf.urls import url 
from . import views

urlpatterns = [
	path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
	]
