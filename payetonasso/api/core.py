from utcaccounts.serializers import UserSerializer

def get_user_basic_info(request):
    user = request.user
    info = UserSerializer.get_info_from_user(user, ['id', 'first_name', 'last_name'])
    return info