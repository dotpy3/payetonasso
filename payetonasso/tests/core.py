from django.contrib import auth

from payemoi.services import tests
from payetonasso.api import core


class tests_core_api(tests.TestCase):

    def test_user_info(self):
        user = auth.get_user_model().objects.create(username='toto', first_name='toto', last_name='dupont',
                                                    email='toto@gmail.com', password='toto')
        user_info = core.UserSerializer.get_info_from_user(user, ['first_name', 'last_name', 'email', 'username'])
        self.assertEqual(user_info['first_name'], user.first_name)
        self.assertEqual(user_info['last_name'], user.last_name)
        self.assertEqual(user_info['email'], user.email)
        self.assertEqual(user_info['username'], user.username)

    def test_user_info_inexistant_user(self):
        user_info = core.UserSerializer.get_info_from_user(None, ['id', 'first_name', 'last_name', 'email', 'username'])
        self.assertIsNone(user_info['id'])
        self.assertIsNone(user_info['first_name'])
        self.assertIsNone(user_info['last_name'])
        self.assertIsNone(user_info['email'])
        self.assertIsNone(user_info['username'])
