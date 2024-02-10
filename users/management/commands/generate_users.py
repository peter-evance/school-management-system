from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone

from users.models import CustomUser

users = [
    {
        "username": "peter",
        "role": CustomUser.RoleChoices.ADMIN,
        "first_name": "peter",
        "last_name": "evance",
        "sex": CustomUser.SexChoices.MALE,
        "date_of_birth": timezone.now().date() - timedelta(weeks=50),
        "password": "string@1234",
        "email": "example@gmail.com",
    },
    {
        "username": "adewale",
        "role": CustomUser.RoleChoices.TEACHER,
        "first_name": "Adewale",
        "last_name": "Johnson",
        "sex": CustomUser.SexChoices.MALE,
        "date_of_birth": timezone.now().date() - timedelta(weeks=50),
        "password": "string@1234",
        "email": "example1@gmail.com",
    },
    {
        "username": "david",
        "role": CustomUser.RoleChoices.STUDENT,
        "first_name": "David",
        "last_name": "Thomas",
        "sex": CustomUser.SexChoices.MALE,
        "date_of_birth": timezone.now().date() - timedelta(weeks=50),
        "password": "string@1234",
        "email": "example2@gmail.com",
    },
]


class Command(BaseCommand):
    help = "creating users from fixture"

    def handle(self, *args, **options):
        for user in users:
            new_user = CustomUser.objects.create_user(**user)
            new_user.approve_user()
        self.stdout.write(self.style.SUCCESS("Users created successfully"))
