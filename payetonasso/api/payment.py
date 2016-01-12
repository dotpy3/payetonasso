from django.core.exceptions import ObjectDoesNotExist

from payemoi.services import payutc

from payetonasso.api import core as api_core


def payment_page(request):
    it = api_core.get_indiv_transaction(request)
    info = dict(transaction=it)
    return info


def initiate_nemopay_payment(request):
    it = api_core.get_indiv_transaction(request)
    nemo_tra = it.get_valid_nemopay_transaction(create_new=True, request=request)
    return nemo_tra.validation_url


def check_nemopay_payment(request):
    nemo_payment = api_core.get_nemo_transaction(request)
    cli = payutc.Client()
    cli.loginApp()
    nemo_info = cli.call('WEBSALE', 'getTransactionInfo', params=None, tra_id=nemo_payment.nemopay_id,
                         fun_id=nemo_payment.inv_transaction.transaction.fundation)
    it = nemo_payment.inv_transaction
    if it.state != 'V':
        it.change_state(state=str(nemo_info['status']))
        it.save()
        nemo_payment.change_state(state=str(nemo_info['status']))
        nemo_payment.save()
