#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from payetonasso.api import dashboard as api_dashboard
from payetonasso.api import payment as api_payment
from payetonasso.api import transactions as api_transactions

default_home = {
    'deactivated': False,
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
def process_new_transaction(request):
    transactions = api_transactions.process_new_transactions(request)
    return JsonResponse(transactions)

def payment(request):
    payment_info = api_payment.payment_page(request)
    return render(request, 'payment/payment_page.html', payment_info)

@login_required
def transactions(request):
    transactions_info = api_transactions.get_transactions(request)
    return render(request, 'transactions/view.html', transactions_info)
