#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from payetonasso.api import dashboard as api_dashboard
from payetonasso.api import transactions as api_transactions

default_home = {
    'deactivated': False,
}

default_dashboard = {
    'id': 0,
    'first_name': 'Prénom',
    'last_name': 'NOM',
    'transactions': [],
}

def home(request):
    return render(request, 'index.html', default_home)

@login_required
def dashboard(request):
    info = api_dashboard.get_dashboard_info(request)
    return render(request, 'dashboard.html', info)

@login_required
def new_transaction(request):
    info = api_transactions.get_new_transactions_info(request)
    return render(request, 'transactions/add.html', info)

@login_required
def transactions(request):
    pass
