# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Company.founded'
        db.add_column(u'ships_company', 'founded',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10, blank=True),
                      keep_default=False)

        # Adding field 'Company.years_operating'
        db.add_column(u'ships_company', 'years_operating',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=15, blank=True),
                      keep_default=False)

        # Adding field 'Company.notes'
        db.add_column(u'ships_company', 'notes',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Company.founded'
        db.delete_column(u'ships_company', 'founded')

        # Deleting field 'Company.years_operating'
        db.delete_column(u'ships_company', 'years_operating')

        # Deleting field 'Company.notes'
        db.delete_column(u'ships_company', 'notes')


    models = {
        u'ships.builder': {
            'Meta': {'object_name': 'Builder', '_ormbases': [u'ships.Company']},
            u'company_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ships.Company']", 'unique': 'True', 'primary_key': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'ships.company': {
            'Meta': {'object_name': 'Company'},
            'founded': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'years_operating': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        u'ships.link': {
            'Meta': {'object_name': 'Link'},
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ships.othername': {
            'Meta': {'object_name': 'OtherName'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'ships.owner': {
            'Meta': {'object_name': 'Owner', '_ormbases': [u'ships.Company']},
            'business': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'company_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ships.Company']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'ships.people': {
            'Meta': {'object_name': 'People'},
            'biog': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birth_year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'ships': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['ships.Ship']", 'null': 'True', 'blank': 'True'})
        },
        u'ships.ship': {
            'Meta': {'object_name': 'Ship'},
            'breadth_in_feet': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'build_year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'builder': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ships.Builder']", 'null': 'True', 'blank': 'True'}),
            'built_for': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'draft_in_feet': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'drive_type': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'history': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_in_feet': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'links': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['ships.Link']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'other_names': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['ships.OtherName']", 'null': 'True', 'blank': 'True'}),
            'previous_owners': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['ships.Owner']", 'null': 'True', 'blank': 'True'}),
            'ship_type': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'yard_no': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'})
        }
    }

    complete_apps = ['ships']