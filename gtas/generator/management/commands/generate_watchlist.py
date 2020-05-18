from django.core.management.base import BaseCommand, CommandError
from gtas.generator.workflow.api.generate_api import GenerateApi
from time import time

class Command(BaseCommand):
    help = "Generate the api files for GTAS"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        start_time = time()
        task = GenerateApi()
        task.run()
        print("--- %s seconds ---" % (time() - start_time))
