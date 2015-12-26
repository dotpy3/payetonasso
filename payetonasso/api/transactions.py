import json
import smtplib

from django.core.exceptions import PermissionDenied

from payemoi.services import payutc
from payetonasso import models
from payetonasso.api import core

def _get_payutc_session_id(request):
    # getting nemopay session id
    return request.COOKIES.get('nemopay_sessionid')

def _get_nemopay_fundations(request):
    cli = payutc.Client(param_session_id=_get_payutc_session_id(request))
    cli.loginApp()
    info = dict(fundations=cli.call('USERRIGHT', 'getAllFundations'))
    return info

def _get_fundation_name(id, fundations_list):
    for fun in fundations_list['fundations']:
        if int(fun['fun_id']) == int(id):
            return fun['name']
    return None

def get_new_transactions_info(request):
    info = _get_nemopay_fundations(request)
    info.update(**core.get_user_basic_info(request))
    return info

def _create_new_transactions(request, information):
    """
    :param request: request, containing the user
    :param information: dict information on the transaction to be created :
        - name : Name of the transaction
        - desc : Description
        - id : PayUTC id
        - amount : Price
        - fundation : Fundation on which to be created
        - individuals : list containing for each :
            - name
            - email
    :return: None
    """
    tc = models.Transaction.objects.create(creator=request.user, name=information['name'],
                                           message=information['desc'], nemopay_article_id=information['id'],
                                           price=information['amount'], fundation=information['fundation'])
    succeeded_mails = []
    failed_mails = []
    for individual in information['individuals']:
        try:
            tc.create_indiv_transaction(individual['name'], individual['email'], request.get_host(),
                                        send_indiv_mail=True,
                                        fun_name=_get_fundation_name(information['fundation'],
                                                                     _get_nemopay_fundations(request)))
            succeeded_mails.append(individual['email'])
        except smtplib.SMTPException as e:
            print(e)
            failed_mails.append(individual['email'])
    return {
        'success': succeeded_mails,
        'fail': failed_mails
    }

def process_new_transactions(request):
    fundations = _get_nemopay_fundations(request)['fundations']
    if int(json.loads(request.body)['fundation']) not in [fun['fun_id'] for fun in fundations]:
        raise PermissionDenied()
    return _create_new_transactions(request, json.loads(request.body))