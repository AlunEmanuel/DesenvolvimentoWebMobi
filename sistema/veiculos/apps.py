from django.apps import AppConfig


class VeiculosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'veiculos'

    def ready(self):
        # Importa signals aqui para evitar imports prematuros que causam
        # "Apps aren't loaded yet." durante makemigrations/migrate.
        from . import signals  # noqa: F401
