from django.apps import AppConfig

import email_app


class EmailAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'email_app'

    def ready(self) -> None:
        import email_app.signals
        return super().ready()
        