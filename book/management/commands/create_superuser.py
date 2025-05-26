from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username="root").exists():
            User.objects.create_superuser("root", "root@gmail.com", "root")
            self.stdout.write("Superuser created.")
        else:
            self.stdout.write("Superuser already exists.")
