# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'News'
        db.create_table(u'news_news', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.DateTimeField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('original_image_width', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('original_image_height', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('thumb_image_width', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('thumb_image_height', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('image', self.gf(u'django.db.models.fields.files.ImageField')(max_length=100)),
            ('min_free_cropping', self.gf(u'django.db.models.fields.CharField')(default=u'', max_length=255, blank=True)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'news', ['News'])


    def backwards(self, orm):
        # Deleting model 'News'
        db.delete_table(u'news_news')


    models = {
        u'news.news': {
            'Meta': {'ordering': "['order']", 'object_name': 'News'},
            'author': ('django.db.models.fields.DateTimeField', [], {}),
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': (u'django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'min_free_cropping': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'original_image_height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'original_image_width': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'thumb_image_height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'thumb_image_width': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['news']