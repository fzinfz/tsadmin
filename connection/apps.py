from django.apps import AppConfig


class ConnectionConfig(AppConfig):
    name = 'connection'
    verbose_name = '连接信息'

    def ready(self):
        import connection.signals