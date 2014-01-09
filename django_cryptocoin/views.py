import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django_cryptocoin.models import CryptoOrder
from django_cryptocoin import settings


def process(request, addr):
    order = get_object_or_404(CryptoOrder, addr=addr)

    return render(request, settings.PROCESS_TEMPLATE, {
        'order': order,
        'confirmations': settings.CONFIRMATIONS[order.currency]
    })


def check_status(request, addr):
    order = get_object_or_404(CryptoOrder, addr=addr)
    response = {
        'received': float(order.amount_received),
        'received_confirmed': float(order.amount_received_confirmed),
        'seconds_remains': order.seconds_remains()
    }

    return HttpResponse(json.dumps(response), content_type="application/json")
