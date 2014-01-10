=================
django-cryptocoin
=================

Django-cryptocoin is a Django app to organize accepting bitcoin, litecoin, novacoin and other cryptocoins, which support JSON-RPC commands getnewaddress and getreceivedbyaddress.

Quick Start
===========

1. Install using pip `pip install django-cryptocoin`

2. Add `'django-cryptocoin',` to INSTALLED_APPS in your `settings.py`

3. Run `python manage.py migrate`

4. Set settings similarly as https://github.com/quantum13/django-crypto-paid-chat/blob/master/cryptochat/settings_local.py-example

5. Add command `python manage.py check_incomings` to cron with interval 1 minute

6. Add relation to CryptoOrder to your order model::

    crypto_order = models.OneToOneField(CryptoOrder, related_name='order')

7. Add handler to payment end signal (delivery digital content, sending email, etc)::

    @receiver(after_pay_confirmation)
    def after_pay(sender, **kwargs):
        pass

8. After sending form with order we need create instance of CryptoOrder and redirect to process view. Example::

        if form.is_valid():
            crypto_order = CryptoOrder(
                currency='btc',
                amount=0.1,#price
                date=timezone.now(),#time of invoice
                redirect_to=reverse('home')#view to redirect after payment
            )
            crypto_order.save()
            form.instance.crypto_order = crypto_order
            form.save()
            return redirect('cryptocoin-order-process', addr=crypto_order.addr)

After confirmation of transaction sended signal `after_pay_confirmation` which handler described above.

Example
=======

https://github.com/quantum13/django-crypto-paid-chat

Tested cryptocoins
==================

- Bitcoin
- Litecoin
- Novacoin
- Emercoin

Options
=======

CRYPTO_COINS
------------
Dict with supported crypto currencies. Default::

    {
        'btc': 'Bitcoin',
        'ltc': 'Litecoin',
        'nvc': 'Novacoin',
    }

CONNECTION_STRING
-----------------
Connection strings for JSON-RPC commands to coin clients. Default::

    {
        'btc': 'your_bitcoin_addr_to_send_btc',
        'ltc': 'your_litecoin_addr_to_send_ltc',
        'nvc': 'your_novacoin_addr_to_send_nvc',
    }

CONFIRMATIONS
-------------
Network confirmations count for each crypto currency. Default::

    {
        'btc': 1,
        'ltc': 1,
        'nvc': 1,
    }

PROCESS_TEMPLATE
----------------
Template for process view. You can use own site template for this page. For example if you have base template `base.html` with block `content` you can create `process.html` in your template folder and paste this code::

    {% extends 'base.html' %}

    {% block content %}
        {% include 'django_cryptocoin/process.html' %}
    {% endblock %}

INVOICE_TIME
------------
How many seconds app will wait for payment. If you set big value, exchange rate to USD can change significantly. Default `900` seconds/

GENERATED_ADDRESSES_ACCOUNT
---------------------------
Account for generated addresses in your wallet. Default `django_cryptocoin`.

CURRENCY_PAIRS
--------------
Currency pairs for which will retrieved exchange rates from btc-e.com. To retrieve this rates run command `python manage.py get_exchange_rates`. Than you can get this rates with function `ExchangeRate.get_exchange_rate(from_currency, to_currency)`. Default::

    ['btc_usd', 'btc_rur', 'btc_eur', 'ltc_usd', 'ltc_rur', 'nvc_usd']



Donate
======

BTC: 1JrV8GW9HWRHWvJNQ14fExAkfgxawAY4oq
LTC: LiHkeymborDtpqUh3ExYT9CXJkyucDH4Cc
NVC: 4U5F4GQin6QkTpbd5k9si3f4iSkn2o3v9x