from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^dashboard$', views.dashboard),
    url(r'^newtransaction$', views.new_transaction),
    url(r'^transactions$', views.transactions),
    url(r'^processtransaction$', views.process_new_transaction),
    url(r'^pay', views.payment),
]
