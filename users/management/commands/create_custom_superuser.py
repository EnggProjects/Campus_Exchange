# users/management/commands/create_custom_superuser.py

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create a custom superuser'

    def handle(self, *args, **options):
        User = get_user_model()
        username = input("Username: ")
        email = input("Email: ")
        password = input("Password: ")
        college = input("College ID (leave blank for None): ")

        user = User(username=username, email=email)
        user.set_password(password)
        
        if college:  # Assuming college is passed as an ID
            try:
                user.college_id = college
            except College.DoesNotExist:
                self.stdout.write(self.style.ERROR("College does not exist!"))
                return

        user.is_superuser = True
        user.is_staff = True
        user.save()
        
        self.stdout.write(self.style.SUCCESS(f"Superuser {username} created successfully."))
