from payemoi import settings


def Log(message):
    if settings.DEBUG:
        print(message)
