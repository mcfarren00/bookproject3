from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings

SuperUser=User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not SuperUser.objects.filter(username=settings.SUPERUSER_NAME).exists():
            SuperUser.objects.create_superuser(
                username=settings.SUPERUSER_NAME,
                email=settings.SUPERUSER_EMAIL,
                password=settings.SUPERUSER_PASSWORD
            )
            print("スーパーユーザー作成")