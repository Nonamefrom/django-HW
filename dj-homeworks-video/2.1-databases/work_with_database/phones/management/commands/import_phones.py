import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for row in phones:
            phone = Phone(
                name=row['name'],
                price=row['price'],
                image=row['image'],
                release_date=row['release_date'],
                lte_exists=row['lte_exists'] == 'True'
            )
            phone.save()
        self.stdout.write(self.style.SUCCESS('Successfully imported phones'))
