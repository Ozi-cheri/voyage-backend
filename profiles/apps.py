from django.apps import AppConfig

class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'

    def ready(self):
        import profiles.signals  # Ensures signals are loaded when app is ready
