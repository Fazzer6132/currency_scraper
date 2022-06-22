from django.core.management.base import BaseCommand

from curr_scraper.apps.api_caller import call_logic


class Command(BaseCommand):

    def handle(self, *args, **options):
        pass

    call_logic.initialize_currency_table()
