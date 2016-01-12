#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render

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

def initiate_payment(request):
    from payemoi.core.utils import Log
    Log('cc')
    nemo_payment_url = api_payment.initiate_nemopay_payment(request)
    return redirect(nemo_payment_url)

def check_payment(request):
    api_payment.check_nemopay_payment(request)
    return HttpResponse('ok')

@login_required
def transactions(request):
    transactions_info = api_transactions.get_transactions(request)
    return render(request, 'transactions/view.html', transactions_info)
