from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.conf.urls import url 
from . import views

urlpatterns = [
    path('<int:form_id>/<int:uid>/cv_score', views.cv_score_getter),
	path('<int:form_id>/<int:uid>/behavior', views.get_behavior_score)
	]
