# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Company'
        db.create_table(u'ships_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'ships', ['Company'])

        # Adding model 'Builder'
        db.create_table(u'ships_builder', (
            (u'company_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ships.Company'], unique=True, primary_key=True)),
            ('nationality', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'ships', ['Builder'])

        # Adding model 'Owner'
        db.create_table(u'ships_owner', (
            (u'company_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ships.Company'], unique=True, primary_key=True)),
            ('business', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'ships', ['Owner'])

        # Adding model 'Link'
        db.create_table(u'ships_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('desc', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'ships', ['Link'])

        # Adding model 'OtherName'
        db.create_table(u'ships_othername', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'ships', ['OtherName'])

        # Adding model 'Ship'
        db.create_table(u'ships_ship', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('ship_type', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('drive_type', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('yard_no', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('build_year', self.gf('django.db.models.fields.CharField')(max_length=4, blank=True)),
            ('built_for', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('length_in_feet', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('breadth_in_feet', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('draft_in_feet', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('previous_owners', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ships.Owner'], null=True, blank=True)),
            ('history', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('links', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ships.Link'], null=True, blank=True)),
            ('other_names', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ships.OtherName'], null=True, blank=True)),
        ))
        db.send_create_signal(u'ships', ['Ship'])


    def backwards(self, orm):
        # Deleting model 'Company'
        db.delete_table(u'ships_company')

        # Deleting model 'Builder'
        db.delete_table(u'ships_builder')

        # Deleting model 'Owner'
        db.delete_table(u'ships_owner')

        # Deleting model 'Link'
        db.delete_table(u'ships_link')

        # Deleting model 'OtherName'
        db.delete_table(u'ships_othername')

        # Deleting model 'Ship'
        db.delete_table(u'ships_ship')


    models = {
        u'ships.builder': {
            'Meta': {'object_name': 'Builder', '_ormbases': [u'ships.Company']},
            u'company_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ships.Company']", 'unique': 'True', 'primary_key': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'ships.company': {
            'Meta': {'object_name': 'Company'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
        u'ships.ship': {
            'Meta': {'object_name': 'Ship'},
            'breadth_in_feet': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'build_year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'built_for': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'draft_in_feet': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'drive_type': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'history': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_in_feet': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'links': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ships.Link']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'other_names': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ships.OtherName']", 'null': 'True', 'blank': 'True'}),
            'previous_owners': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ships.Owner']", 'null': 'True', 'blank': 'True'}),
            'ship_type': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'yard_no': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'})
        }
    }

    complete_apps = ['ships']