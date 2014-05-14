# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Dispatcher'
        db.create_table(u'monitor_dispatcher', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip_address', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39)),
        ))
        db.send_create_signal(u'monitor', ['Dispatcher'])

        # Adding model 'ProviderAgent'
        db.create_table(u'monitor_provideragent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip_address', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39)),
            ('agent_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'monitor', ['ProviderAgent'])


    def backwards(self, orm):
        # Deleting model 'Dispatcher'
        db.delete_table(u'monitor_dispatcher')

        # Deleting model 'ProviderAgent'
        db.delete_table(u'monitor_provideragent')


    models = {
        u'monitor.dispatcher': {
            'Meta': {'object_name': 'Dispatcher'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'})
        },
        u'monitor.provideragent': {
            'Meta': {'object_name': 'ProviderAgent'},
            'agent_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'})
        }
    }

    complete_apps = ['monitor']