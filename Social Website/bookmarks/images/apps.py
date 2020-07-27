from django.apps import AppConfig


class ImagesConfig(AppConfig):
    name = 'images'

    # Функция ready() требуется для регистрации сигналов
    def ready(self):
        import images.signals
