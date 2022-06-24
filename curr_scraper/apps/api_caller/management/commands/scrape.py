from curr_scraper.apps.api_caller import call_logic
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('base_currency', type=str)

    def handle(self, *args, **options):
        call_logic.scrape_data(options['base_currency'])



