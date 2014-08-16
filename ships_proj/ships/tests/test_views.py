from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from ships.models import *

class ShipIndexTest(TestCase):

    def test_home_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'ships/ships.html')

    def test_displays_ships_list(self):
        correct_ships = Ship.objects.create(name='Cutty Sark',
            yard_no='46', build_year='1867', history='torched')
        response = self.client.get('/')
        self.assertContains(response, 'Cutty Sark')

class ShipDetailView(TestCase):

    def test_detail_view_uses_correct_template(self):
        ship = Ship.objects.create(name='Cutty Sark',
                            yard_no='46', build_year='1867', history='torched')
        response = self.client.get('/%d/' % ship.id)
        self.assertTemplateUsed(response, 'ships/ship_detail.html')

    def test_passes_correct_ship_to_template(self):
        ship1 = Ship.objects.create(name='Cutty Sark',
            yard_no='46', build_year='1867', history='torched')
        ship2 = Ship.objects.create(name='City of Abelaide', yard_no='12', build_year='1865', history="transferred migrants to Oz")
        response = self.client.get('/%d/' % ship1.id)
        self.assertEqual(response.context['ship'], ship1)

