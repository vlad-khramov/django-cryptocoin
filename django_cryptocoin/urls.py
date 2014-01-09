from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^process/(?P<addr>.+)$', 'django_cryptocoin.views.process', name='cryptocoin-order-process'),
    url(r'^check_status/(?P<addr>.+)$', 'django_cryptocoin.views.check_status', name='cryptocoin-order-check-status'),
)
