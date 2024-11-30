import time

from django.core.management import BaseCommand
from django.db import OperationalError, connection
from django.db.backends.mysql.base import DatabaseWrapper

connection: DatabaseWrapper = connection


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Waiting for database...'))
        connection_db = False

        while not connection_db:
            try:
                connection.ensure_connection()
                connection_db = True
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 3 second...')
                time.sleep(3)

        self.stdout.write(self.style.SUCCESS('Database available!'))
