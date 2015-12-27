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
