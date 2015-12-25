from django.contrib import auth

USER_MODEL = auth.get_user_model()


class UserSerializer:

    @classmethod
    def get_user_as_dict(cls, user):
        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'email': user.email,
        }

    @classmethod
    def get_info_from_user(cls, user, fields):
        user_as_dict = cls.get_user_as_dict(user)
        return { attr: user_as_dict[attr] for attr in fields }
