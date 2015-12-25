# -*- coding: utf-8 -*-

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User as USER_MODEL


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
    notify_creator = models.BooleanField(default=False)
    # Indicates if the creator wants to receive an e-mail when validated
    created = models.DateTimeField(default=timezone.now)
    # time at which the transaction was created by the user


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

    transaction = models.ForeignKey(Transaction)
    # transaction of which it is a part of
    validation = models.DateTimeField(null=True,default=None)
    # time at which the transaction was recognized as validated by the server
    user_name = models.CharField(max_length=50)
    # receiver's name
    user_email = models.CharField(max_length=50)
    # receiver's email

class NemopayTransaction(DifferentState):

    inv_transaction = models.ForeignKey(IndividualTransaction)
    # individual transaction to which the nemopay transaction is associated
    created = models.DateTimeField(default=timezone.now)
    # time at which the transaction was created by the user
    nemopay_id = models.IntegerField(null=True, default=None)
    # Nemopay transaction ID
