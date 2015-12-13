from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^dashboard$', views.dashboard),
]
