import requests

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from payemoi.settings import NEMOPAY_API_URL, NEMOPAY_SYSTEM_ID, NEMOPAY_LOGIN_SERVICE

class Client:

    SESSION_ID = None

    app_login = False
    user_login = False

    def logged(self):
        return {
            'user': self.user_login,
            'app': self.app_login,
        }

    def loginCas(self, ticket, service):
        url = self._call_url(NEMOPAY_LOGIN_SERVICE, 'loginCas') + '?system_id=' + NEMOPAY_SYSTEM_ID
        r = requests.post(url, data={ 'ticket': ticket, 'service': service })
        return str(r.text.strip('"'))

    def _call_url(self, service, method):
        return NEMOPAY_API_URL + service + '/' + method

    def call(self, service, method, **params):
        r = requests.post(NEMOPAY_API_URL + service + '/' + method)
        self._call_url(service)


class PayUTCAuthBackend(ModelBackend):
    """Login to Django using just the user login
    """
    def authenticate(self, username=None):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
