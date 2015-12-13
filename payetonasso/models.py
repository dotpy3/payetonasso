from datetime import datetime
from django.db import models

from utcaccounts.models import CasAccount

class AssoKey(models.Model):

    ROLE_GESARTICLE = 'GESARTICLES'
    # Not yet implemented

    ROLE_WEBSALE = 'WEBSALE'

    ROLES = (
        (ROLE_GESARTICLE, 'Gestion des articles'),
        (ROLE_WEBSALE, 'Encaissement en ligne'),
    )

    user = models.ForeignKey(CasAccount, related_name="keys_set")
    # user that is associated to the key
    name = models.CharField(max_length=50)
    # name given to the user by the key
    key = models.CharField(max_length=50)
    # Nemopay API key
    fundation_id = models.IntegerField()
    # PayUTC fundation id
    type = models.CharField(max_length=100, default=ROLE_WEBSALE, choices=ROLES)
    # key type


class Transaction(models.Model):

    creator = models.ForeignKey(CasAccount, related_name="user_generated_transactions_set")
    # user that created the transaction
    generator_key = models.ForeignKey(AssoKey, related_name="key_generated_transactions_set")
    # WEBSALE payutc key used to generate the transaction
    name = models.CharField(max_length=256)
    # name of the transaction
    message = models.TextField(blank=True, default='')
    # description of the transaction, send to the receiver by mail
    payutc_id = models.IntegerField(null=True, default=None)
    # PayUTC ID of the transaction
    notify_creator = models.BooleanField(default=False)
    # Indicates if the creator wants to receive an e-mail when validated
    creation = models.DateTimeField(default=datetime.now())
    # time at which the transaction was created by the user


class TransactionRow(models.Model):

    STATE_INVALID = 'W'
    STATE_ABORTED = 'A'
    STATE_VALID = 'V'

    STATES = (
        (STATE_VALID, 'Validée'),
        (STATE_ABORTED, 'Annulée'),
        (STATE_INVALID, 'En cours'),
    )

    validation = models.DateTimeField(null=True,default=None)
    # time at which the transaction was recognized as validated by the server
    user_name = models.CharField(max_length=50)
    # receiver's name
    user_email = models.CharField(max_length=50)
    # receiver's email
