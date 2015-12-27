from payetonasso import models
from payetonasso.api import core

def get_dashboard_info(request):
    info = core.get_user_basic_info(request)
    info['waiting_transactions'] = models.IndividualTransaction.objects.\
        filter(state=models.IndividualTransaction.STATE_INVALID).count()
    info['validated_transactions'] = models.IndividualTransaction.objects.\
        filter(state=models.IndividualTransaction.STATE_VALID).count()
    info['last_validated'] = core._get_user_transactions(request, limit=5, notnull_filter='validation')
    return info
