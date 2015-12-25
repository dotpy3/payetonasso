from payetonasso import models
from utcaccounts.serializers import UserSerializer

def get_dashboard_info(request):
    user = request.user
    info = UserSerializer.get_info_from_user(user, ['id', 'first_name', 'last_name'])
    info['waiting_transactions'] = models.IndividualTransaction.objects.\
        filter(state=models.IndividualTransaction.STATE_INVALID).count()
    info['validated_transactions'] = models.IndividualTransaction.objects.\
        filter(state=models.IndividualTransaction.STATE_VALID).count()
    return info
