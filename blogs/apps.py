from django.apps import AppConfig


class BlogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogs'

class BlogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogs'

    def ready(self):
        import blogs.signals


      