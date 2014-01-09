from django.conf import settings

CRYPTO_COINS = getattr(
    settings,
    "CRYPTO_COINS",
    {
        'btc': 'Bitcoin',
        'ltc': 'Litecoin',
        'nvc': 'Novacoin',
    }
)

CONNECTION_STRING = getattr(
    settings,
    "CONNECTION_STRING",
    {
        'btc': 'http://user:pass@localhost:8332',
        'ltc': 'http://user:pass@localhost:9332',
        'nvc': 'http://user:pass@localhost:8344',
    }
)

MAIN_ADDR = getattr(
    settings,
    "MAIN_ADDR",
    {
        'btc': 'your_bitcoin_addr_to_send_btc',
        'ltc': 'your_litecoin_addr_to_send_ltc',
        'nvc': 'your_novacoin_addr_to_send_nvc',
    }
)

CONFIRMATIONS = getattr(
    settings,
    "CONFIRMATIONS",
    {
        'btc': 1,
        'ltc': 2,
        'nvc': 3,
    }
)

PROCESS_TEMPLATE = getattr(
    settings,
    "PROCESS_TEMPLATE",
    'django_cryptocoin/process.html'
)

INVOICE_TIME = getattr(
    settings,
    "INVOICE_TIME",
    600
)

GENERATED_ADDRESSES_ACCOUNT = getattr(
    settings,
    "GENERATED_ADDRESSES_ACCOUNT",
    'django_cryptocoin'
)



#currency pairs for which will retrieved exchange rate from btc-e
CURRENCY_PAIRS = getattr(
    settings,
    "CURRENCY_PAIRS",
    ['btc_usd', 'btc_rur', 'btc_eur', 'ltc_usd', 'ltc_rur', 'nvc_usd']
)
