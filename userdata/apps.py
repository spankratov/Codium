from django.apps import AppConfig

class UserdataConfig(AppConfig):
    name = 'userdata'
    verbose_name = 'User-related information'

    def ready(self):
        import userdata.signals