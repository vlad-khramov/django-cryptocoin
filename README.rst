=================
django-cryptocoin
=================

Django-cryptocoin is a Django app to organize accepting bitcoin, litecoin, novacoin and other cryptocoins.

Quick Start
===========

1. Install using pip:

        pip install django-cryptocoin

2. Add to INSTALLED_APPS in your `settings.py`:

        'django-cryptocoin',

3. Run `python manage.py migrate`

4. ...


Example
=======

https://github.com/quantum13/django-crypto-paid-chat


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
    {% load crispy_forms_tags %}

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