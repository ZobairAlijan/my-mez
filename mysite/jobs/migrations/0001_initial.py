# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Jobs'
        db.create_table(u'jobs_jobs', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('background', self.gf('django.db.models.fields.CharField')(max_length=500, null=True)),
            ('Core_Technologies', self.gf('django.db.models.fields.CharField')(max_length=500, null=True)),
            ('Skills', self.gf('django.db.models.fields.CharField')(max_length=500, null=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=500, null=True)),
            ('benefits', self.gf('django.db.models.fields.CharField')(max_length=500, null=True)),
            ('Applying', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True)),
            ('Responsibilities', self.gf('django.db.models.fields.CharField')(max_length=500, null=True)),
            ('Referrals', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'jobs', ['Jobs'])


    def backwards(self, orm):
        # Deleting model 'Jobs'
        db.delete_table(u'jobs_jobs')


    models = {
        u'jobs.jobs': {
            'Applying': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'Core_Technologies': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'Meta': {'object_name': 'Jobs'},
            'Referrals': ('django.db.models.fields.TextField', [], {}),
            'Responsibilities': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'Skills': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'background': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'benefits': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'})
        }
    }

    complete_apps = ['jobs']