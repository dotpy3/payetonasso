#-*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from settings import UTC_CAS_URL

from .utils import CASTicket, user_creation

def dashboard_redirection():
    return redirect('payetonasso.dashboard')

def connexion_cas(request):
    if request.user.is_authenticated():
        return dashboard_redirection()
    ticket = request.GET.get('ticket', '')
    if ticket is None or ticket == '':
        return redirect(UTC_CAS_URL + 'login/?service=' + request.build_absolute_uri())
    else:
        user_ticket = CASTicket(request.build_absolute_uri().split('?')[0], ticket)
        login_given = user_ticket.get_information()
        # at this point, login_given contains the CAS login
        print(login_given)
        user = authenticate(username=login_given)
        if user is None:
            print("auth failed")
            user = user_creation(login_given)
        if user.is_active:
            user = authenticate(username=login_given)
            login(request, user)
        else:
            return redirect('payetonasso.home', { 'deactivated': True })
        return dashboard_redirection()

