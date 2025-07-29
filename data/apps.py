from django.apps import AppConfig

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'data'  # substitua pelo nome real do seu app

    def ready(self):
        import data.signals  # substitua pelo nome real do app
