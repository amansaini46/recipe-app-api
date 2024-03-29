import time

from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """"Wait until DB is available"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database....')
        db_up = False
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Waiting for DB will try again in 1 seconds')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
