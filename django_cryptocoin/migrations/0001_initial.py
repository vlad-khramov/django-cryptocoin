# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CryptoOrder'
        db.create_table(u'django_cryptocoin_cryptoorder', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('currency', self.gf('django.db.models.fields.CharField')(default='btc', max_length=50)),
            ('addr', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=18, decimal_places=8)),
            ('amount_received', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=18, decimal_places=8)),
            ('amount_received_confirmed', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=18, decimal_places=8)),
            ('redirect_to', self.gf('django.db.models.fields.CharField')(default='/', max_length=200)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('processed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'django_cryptocoin', ['CryptoOrder'])

        # Adding model 'ExchangeRate'
        db.create_table(u'django_cryptocoin_exchangerate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('currency1', self.gf('django.db.models.fields.CharField')(default='btc', max_length=50)),
            ('currency2', self.gf('django.db.models.fields.CharField')(default='usd', max_length=50)),
            ('rate', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=18, decimal_places=8)),
        ))
        db.send_create_signal(u'django_cryptocoin', ['ExchangeRate'])


    def backwards(self, orm):
        # Deleting model 'CryptoOrder'
        db.delete_table(u'django_cryptocoin_cryptoorder')

        # Deleting model 'ExchangeRate'
        db.delete_table(u'django_cryptocoin_exchangerate')


    models = {
        u'django_cryptocoin.cryptoorder': {
            'Meta': {'object_name': 'CryptoOrder'},
            'addr': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '18', 'decimal_places': '8'}),
            'amount_received': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '18', 'decimal_places': '8'}),
            'amount_received_confirmed': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '18', 'decimal_places': '8'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'btc'", 'max_length': '50'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'processed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'redirect_to': ('django.db.models.fields.CharField', [], {'default': "'/'", 'max_length': '200'})
        },
        u'django_cryptocoin.exchangerate': {
            'Meta': {'object_name': 'ExchangeRate'},
            'currency1': ('django.db.models.fields.CharField', [], {'default': "'btc'", 'max_length': '50'}),
            'currency2': ('django.db.models.fields.CharField', [], {'default': "'usd'", 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '18', 'decimal_places': '8'})
        }
    }

    complete_apps = ['django_cryptocoin']