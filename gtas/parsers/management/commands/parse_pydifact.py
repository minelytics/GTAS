from django.core.management.base import BaseCommand, CommandError
from time import time

class Command(BaseCommand):
    help = "Parse an example using the pydifact for GTAS"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        start_time = time()
        print("--- %s seconds ---" % (time() - start_time))
