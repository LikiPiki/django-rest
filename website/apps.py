from django.apps import AppConfig


class WebsiteConfig(AppConfig):
    name = 'website'

    def __str__(self):
        return self.name
