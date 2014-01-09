import httplib
import json
from django.core.management.base import BaseCommand
from django_cryptocoin.models import ExchangeRate
from django_cryptocoin import settings


class Command(BaseCommand):
    args = ''
    help = 'Executes parsing exchange rates from btc-e.com'

    def handle(self, *args, **options):

        for pair in settings.CURRENCY_PAIRS:
            currencies = pair.split('_')
            conn = httplib.HTTPSConnection("btc-e.com")
            conn.request("GET", "/api/2/%s/ticker" % pair)
            response = conn.getresponse()
            rate, created = ExchangeRate.objects.get_or_create(currency1=currencies[0], currency2=currencies[1])
            json_resp = json.load(response)
            rate.rate = json_resp['ticker']['last']
            rate.save()


        self.stdout.write('Successfully executed')