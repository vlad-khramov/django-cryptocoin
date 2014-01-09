import json
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django_cryptocoin.models import CryptoOrder
from django_cryptocoin.settings import PROCESS_TEMPLATE, CRYPTO_COINS, INVOICE_TIME, CONFIRMATIONS


def process(request, addr):
    order = get_object_or_404(CryptoOrder, addr=addr)

    return render(request, PROCESS_TEMPLATE, {
        'order': order,
        'confirmations': CONFIRMATIONS[order.currency]
    })


def check_status(request, addr):
    order = get_object_or_404(CryptoOrder, addr=addr)
    response = {
        'received': float(order.amount_received),
        'received_confirmed': float(order.amount_received_confirmed),
        'seconds_remains': order.seconds_remains()
    }

    return HttpResponse(json.dumps(response), content_type="application/json")
