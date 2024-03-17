from django.apps import AppConfig

# механизм конфигурации приложения позволяет определить, 
# как мое приложение должно вести себя при запуске

class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"

    #Следующая функция с импортом гарантирует что сигналы определенные в файле signals приложения users
    #будут загружены и готовы к использованию при запуске моего приложения.
    def ready(self):
        import users.signals
