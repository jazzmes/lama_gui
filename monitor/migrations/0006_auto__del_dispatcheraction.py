# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'DispatcherAction'
        db.delete_table('monitor_dispatcheraction')


    def backwards(self, orm):
        # Adding model 'DispatcherAction'
        db.create_table('monitor_dispatcheraction', (
            ('dispatcher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitor.Dispatcher'])),
            ('last_run', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('monitor', ['DispatcherAction'])


    models = {
        'monitor.dispatcher': {
            'Meta': {'object_name': 'Dispatcher'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'})
        },
        'monitor.provideragent': {
            'Meta': {'object_name': 'ProviderAgent'},
            'agent_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.GenericIPAddressField', [], {'unique': 'True', 'max_length': '39'}),
            'last_seen': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True', 'auto_now_add': 'True'})
        }
    }

    complete_apps = ['monitor']