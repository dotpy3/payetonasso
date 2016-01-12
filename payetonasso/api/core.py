from django.core.exceptions import ObjectDoesNotExist

from payetonasso import models
from utcaccounts.serializers import UserSerializer


def get_user_basic_info(request):
    user = request.user
    info = UserSerializer.get_info_from_user(user, ['id', 'first_name', 'last_name'])
    return info


def _get_user_transactions(request, limit=None, notnull_filter=None):
    user = request.user
    transactions = models.IndividualTransaction.objects.filter(transaction__creator=user).\
        values('transaction__name', 'transaction__message', 'user_name', 'user_email', 'transaction__created',
               'transaction__fundation_name', 'state', 'transaction__nemopay_article_id', 'transaction__price',
               'validation').order_by('-transaction__created')
    if notnull_filter is not None:
        transactions = transactions.filter(**{ notnull_filter+'__isnull': False })
    if limit is not None:
        transactions = transactions[:limit]
    return transactions


def get_transaction(model, request, exception=True):
    # exception : means whether an exception should be raised if no transaction
    # Get transaction number from the url
    transaction_id = int(request.GET['transaction'])
    try:
        return model.objects.get(pk=transaction_id)
    except model.DoesNotExist:
        if exception:
            raise ObjectDoesNotExist()
        else:
            return None


def get_indiv_transaction(request, exception=True):
    return get_transaction(models.IndividualTransaction, request, exception)


def get_nemo_transaction(request, exception=True):
    return get_transaction(models.NemopayTransaction, request, exception)
