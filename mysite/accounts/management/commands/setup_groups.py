from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Create default groups for the application'

    def handle(self, *args, **options):
        # Create CUSTOMER group
        customer_group, created = Group.objects.get_or_create(name='CUSTOMER')
        if created:
            self.stdout.write(
                self.style.SUCCESS('Successfully created CUSTOMER group')
            )
        else:
            self.stdout.write(
                self.style.WARNING('CUSTOMER group already exists')
            )

        # Create ADMIN group
        admin_group, created = Group.objects.get_or_create(name='ADMIN')
        if created:
            self.stdout.write(
                self.style.SUCCESS('Successfully created ADMIN group')
            )
        else:
            self.stdout.write(
                self.style.WARNING('ADMIN group already exists')
            )

        # Create CASHIER group
        cashier_group, created = Group.objects.get_or_create(name='CASHIER')
        if created:
            self.stdout.write(
                self.style.SUCCESS('Successfully created CASHIER group')
            )
        else:
            self.stdout.write(
                self.style.WARNING('CASHIER group already exists')
            ) 