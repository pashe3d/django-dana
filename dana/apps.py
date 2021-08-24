from django.apps import AppConfig


class DanaConfig(AppConfig):
    name = 'dana'

    def ready(self):
        import dana.signals  # noqa
