#-*- coding: utf-8 -*-

import urllib2

from django.shortcuts import redirect

from settings import UTC_CAS_URL

def connexion_cas(request):
    ticket = request.GET.get('ticket', '')
    if ticket is None or ticket == '':
        return redirect(UTC_CAS_URL + 'login/?service=' + request.build_absolute_uri())
    else:
    

# Create your views here.
