from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.all_users.users'

    def ready(self):
        import apps.all_users.users.signals
