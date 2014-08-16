# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Ship.previous_owners'
        db.delete_column(u'ships_ship', 'previous_owners_id')

        # Deleting field 'Ship.other_names'
        db.delete_column(u'ships_ship', 'other_names_id')

        # Deleting field 'Ship.links'
        db.delete_column(u'ships_ship', 'links_id')

        # Adding M2M table for field previous_owners on 'Ship'
        m2m_table_name = db.shorten_name(u'ships_ship_previous_owners')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ship', models.ForeignKey(orm[u'ships.ship'], null=False)),
            ('owner', models.ForeignKey(orm[u'ships.owner'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ship_id', 'owner_id'])

        # Adding M2M table for field links on 'Ship'
        m2m_table_name = db.shorten_name(u'ships_ship_links')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ship', models.ForeignKey(orm[u'ships.ship'], null=False)),
            ('link', models.ForeignKey(orm[u'ships.link'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ship_id', 'link_id'])

        # Adding M2M table for field other_names on 'Ship'
        m2m_table_name = db.shorten_name(u'ships_ship_other_names')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ship', models.ForeignKey(orm[u'ships.ship'], null=False)),
            ('othername', models.ForeignKey(orm[u'ships.othername'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ship_id', 'othername_id'])


    def backwards(self, orm):
        # Adding field 'Ship.previous_owners'
        db.add_column(u'ships_ship', 'previous_owners',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ships.Owner'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Ship.other_names'
        db.add_column(u'ships_ship', 'other_names',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ships.OtherName'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Ship.links'
        db.add_column(u'ships_ship', 'links',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ships.Link'], null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field previous_owners on 'Ship'
        db.delete_table(db.shorten_name(u'ships_ship_previous_owners'))

        # Removing M2M table for field links on 'Ship'
        db.delete_table(db.shorten_name(u'ships_ship_links'))

        # Removing M2M table for field other_names on 'Ship'
        db.delete_table(db.shorten_name(u'ships_ship_other_names'))


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
        u'ships.people': {
            'Meta': {'object_name': 'People'},
            'biog': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birth_year': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ships': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['ships.Ship']", 'null': 'True', 'blank': 'True'})
        },
        u'ships.ship': {
            'Meta': {'object_name': 'Ship'},
            'breadth_in_feet': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'build_year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
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