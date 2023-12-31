from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone

from users.models import CustomUser

users = [
    {
        "username": "adewale",
        "role": CustomUser.RoleChoices.TEACHER,
        "first_name": "Adewale",
        "last_name": "Johnson",
        "sex": CustomUser.SexChoices.MALE,
        "date_of_birth": timezone.now().date() - timedelta(weeks=50),
        "password": "string@1234",
    },
    {
        "username": "peter",
        "role": CustomUser.RoleChoices.ADMIN,
        "first_name": "peter",
        "last_name": "evance",
        "sex": CustomUser.SexChoices.MALE,
        "date_of_birth": timezone.now().date() - timedelta(weeks=50),
        "password": "string@1234",
    }
]


class Command(BaseCommand):
    help = "creating users from fixture"

    def handle(self, *args, **options):
        for user in users:
            CustomUser.objects.create_user(**user)
        self.stdout.write(self.style.SUCCESS("Users created successfully"))
