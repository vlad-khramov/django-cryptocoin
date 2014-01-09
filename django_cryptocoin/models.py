from django.db import models
from django.utils import timezone
from bitcoinrpc.authproxy import AuthServiceProxy
from django_cryptocoin import settings


class CryptoOrder(models.Model):
    currency = models.CharField(max_length=50, default='btc', choices=settings.CRYPTO_COINS.items())
    addr = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=18, decimal_places=8)
    amount_received = models.DecimalField(max_digits=18, decimal_places=8, default=0)
    amount_received_confirmed = models.DecimalField(max_digits=18, decimal_places=8, default=0)
    redirect_to = models.CharField(max_length=200, default='/')
    date = models.DateTimeField()
    processed = models.BooleanField(default=False)

    def seconds_remains(self):
        return settings.INVOICE_TIME - (timezone.now() - self.date).seconds

    def currency_full(self):
        return settings.CRYPTO_COINS[self.currency]

    def save(self, *args, **kwargs):
        if self.pk is None:
            if not self.currency in settings.CONNECTION_STRING:
                raise Exception("Connection string for %s is not defined" % self.currency)
            try:
                access = AuthServiceProxy(settings.CONNECTION_STRING[self.currency])
                self.addr = access.getnewaddress(settings.GENERATED_ADDRESSES_ACCOUNT)
            except Exception, e:
                raise Exception("Could not connect to crypto coin daemon")

        super(CryptoOrder, self).save(*args, **kwargs)


class ExchangeRate(models.Model):
    currency1 = models.CharField(max_length=50, default='btc')
    currency2 = models.CharField(max_length=50, default='usd')
    rate = models.DecimalField(max_digits=18, decimal_places=8, default=0)

    @classmethod
    def get_exchange_rate(cls, from_currency, to_currency):
        """Get rate to exchange from real money to cryprocoins"""
        try:
           rate = ExchangeRate.objects.get(currency2=from_currency, currency1=to_currency)
        except Exception, e:
            raise Exception("Could not get exchange rate for this currencies")

        return 1/rate.rate