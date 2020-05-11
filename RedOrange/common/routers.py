from rest_framework import routers


class PUTNotAllowedRouter(routers.SimpleRouter):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            del cls._instance.routes[2].mapping['put']
        return cls._instance
