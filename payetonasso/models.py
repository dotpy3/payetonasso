# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

from django.core.mail import send_mail
from django.contrib.auth.models import User as USER_MODEL
from django.db import models
from django.template.loader import get_template
from django.utils.timezone import utc

from payemoi.services import payutc
from payemoi.settings import DEFAULT_FROM_EMAIL

from payetonasso.api import requests as api_requests


class Transaction(models.Model):

    creator = models.ForeignKey(USER_MODEL, related_name="user_generated_transactions_set")
    # user that created the transaction
    name = models.CharField(max_length=256)
    # name of the transaction
    message = models.TextField(blank=True, default='')
    # description of the transaction, send to the receiver by mail
    nemopay_article_id = models.IntegerField(null=True, default=None)
    # Nemopay ID of the transaction
    price = models.FloatField(default=0)
    # Price of the transaction
    fundation = models.IntegerField(default=0)
    # Fundation ID
    fundation_name = models.CharField(max_length=256, default='PayUTC')
    # Fundation name
    notify_creator = models.BooleanField(default=False)
    # Indicates if the creator wants to receive an e-mail when validated
    created = models.DateTimeField(auto_now_add=True)
    # time at which the transaction was created by the user

    def create_indiv_transaction(self, name, email, request, fun_name=None, send_indiv_mail=False):
        it = IndividualTransaction.objects.create(transaction=self, user_name=name, user_email=email)
        if send_indiv_mail:
            mail_template = get_template('mails/payment_invitation.html')
            mail_context = { 'fun_name': fun_name, 't': self, 'id': it.id,
                             'url': api_requests.build_uri(request, '/paymentpage')}
            html_content = mail_template.render(mail_context)
            send_mail('Vous avez un demande de paiement de '+self.fundation_name+' sur Paye ton Asso!',
                      'Pour lire ce message, merci d\'utiliser un navigateur ou un client mail compatible HTML.',
                      DEFAULT_FROM_EMAIL, [email], html_message=html_content)


class DifferentState(models.Model):

    STATE_INVALID = 'W'
    STATE_ABORTED = 'A'
    STATE_VALID = 'V'

    STATES = (
        (STATE_VALID, 'Validée'),
        (STATE_ABORTED, 'Annulée'),
        (STATE_INVALID, 'En cours'),
    )

    state = models.CharField(max_length=1, choices=STATES, default=STATE_INVALID)
    # state of the individual transaction

    def change_state(self, state):
        self.state = state

    class Meta:
        abstract = True


class IndividualTransaction(DifferentState):

    transaction = models.ForeignKey(Transaction, null=True)
    # transaction of which it is a part of
    validation = models.DateTimeField(null=True,default=None)
    # time at which the transaction was recognized as validated by the server
    user_name = models.CharField(max_length=256)
    # receiver's name
    user_email = models.CharField(max_length=256)
    # receiver's email

    def change_state(self, state):
        self.state = state
        if state == 'V':
            self.validation = datetime.now()
            self.validation_mail_process()

    def get_valid_nemopay_transaction(self, create_new=True, request=None):
        last_nemo_transaction = self.nemopaytransaction_set.last()
        if last_nemo_transaction and (last_nemo_transaction.is_valid() or self.validation):
            return last_nemo_transaction
        else:
            if create_new:
                new_nemo_transaction = self.new_nemopay_transaction(request=request)
                return new_nemo_transaction
            else:
                return None

    def validation_mail_process(self):
        if self.transaction.notify_creator:
            t = self.transaction
            mail_template = get_template('mails/payment_confirmation.html')
            mail_context = { 'amount': t.price, 'user_name': self.user_name,
                             'transaction_name': t.name, 'fundation': t.fundation_name }
            html_content = mail_template.render(mail_context)
            send_mail('Une transaction a été validée sur Paye ton Asso!',
                      'Pour lire ce mail, merci d\'utilisateur un navigateur ou client compatible HTML.',
                      DEFAULT_FROM_EMAIL, [self.user_email], html_message=html_content)

    def new_nemopay_transaction(self, request):
        cli = payutc.Client()
        cli.loginApp()
        tr = self.transaction
        nemo_transaction = NemopayTransaction.objects.create(inv_transaction=self)
        nemo_info = cli.call('WEBSALE', 'createTransaction', params=None, fun_id=tr.fundation,
                             items='[['+str(tr.nemopay_article_id)+']]', mail=self.user_email,
                             return_url='https://payutc.nemopay.net',
                             callback_url=nemo_transaction.generate_callback_url(request=request))
        nemo_transaction.validation_url = nemo_info['url']
        nemo_transaction.nemopay_id = nemo_info['tra_id']
        nemo_transaction.save()
        return nemo_transaction

class NemopayTransaction(DifferentState):

    inv_transaction = models.ForeignKey(IndividualTransaction)
    # individual transaction to which the nemopay transaction is associated
    created = models.DateTimeField(auto_now_add=True)
    # time at which the transaction was created by the user
    nemopay_id = models.IntegerField(null=True, default=None)
    # Nemopay transaction ID
    validation_url = models.CharField(max_length=256, null=True, default=None)
    # Nemopay payment URL

    def generate_callback_url(self, request):
        return api_requests.build_uri(request, '/checkpayment') + '?transaction=' + str(self.pk)

    def is_expired(self):
        """
        After 50 minutes, a Nemopay WEBSALE transaction weblink cannot be accessed anymore.
        After 60 minutes, the transaction cannot be completed.
        """
        now = datetime.utcnow().replace(tzinfo=utc)
        delta = now - self.created
        max_delta = timedelta(minutes=50)
        if delta > max_delta:
            return False
        else:
            return True

    def is_valid(self):
        return not self.is_expired()
