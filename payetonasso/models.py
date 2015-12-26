# -*- coding: utf-8 -*-

from django.core.mail import send_mail
from django.contrib.auth.models import User as USER_MODEL
from django.db import models
from django.template import Context
from django.template.loader import get_template
from django.utils import timezone

from payemoi.settings import DEFAULT_FROM_EMAIL


class Transaction(models.Model):

    creator = models.ForeignKey(USER_MODEL, related_name="user_generated_transactions_set")
    # user that created the transaction
    name = models.CharField(max_length=256)
    # name of the transaction
    message = models.TextField(blank=True, default='')
    # description of the transaction, send to the receiver by mail
    nemopay_article_id = models.IntegerField(null=True, default=None)
    # Nemopay ID of the transaction
    price = models.IntegerField(default=0)
    # Price of the transaction
    fundation = models.IntegerField(default=0)
    # Fundation ID
    notify_creator = models.BooleanField(default=False)
    # Indicates if the creator wants to receive an e-mail when validated
    created = models.DateTimeField(default=timezone.now)
    # time at which the transaction was created by the user

    def create_indiv_transaction(self, name, email, host, fun_name=None, send_indiv_mail=False):
        it = IndividualTransaction.objects.create(transaction=self, user_name=name, user_email=email)
        if send_indiv_mail:
            mail_template = get_template('mails/payment_invitation.html')
            mail_context = Context({ 'fun_name': fun_name, 't': self, 'id': it.id, 'host': host })
            html_content = mail_template.render(mail_context)
            send_mail('Vous avez un paiement en attente sur Paye ton Asso!', 'Pour lire ce message, merci d'
                      'utiliser un navigateur ou un client mail compatible HTML.', DEFAULT_FROM_EMAIL, [email],
                      html_message=html_content)


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

class NemopayTransaction(DifferentState):

    inv_transaction = models.ForeignKey(IndividualTransaction)
    # individual transaction to which the nemopay transaction is associated
    created = models.DateTimeField(default=timezone.now)
    # time at which the transaction was created by the user
    nemopay_id = models.IntegerField(null=True, default=None)
    # Nemopay transaction ID
