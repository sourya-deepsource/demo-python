from django.apps import AppConfig


class BobbyConfig(AppConfig):
    name = "Bobby"

    def ready(self):
        """Application bootstrap."""
        # pylint:disable=unused-import
        from . import receivers
