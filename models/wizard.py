# -*- coding: UTF-8 -*-
'''
    country.model.wizard

    Wizard which adds the country itself and subdivisions
    of a country to the openerp database

    :copyright: (c) 2010 by Openlabs technologies & Consulting (P) LTD
    :license: AGPL, see LICENSE for more details
'''

import pycountry

from osv import osv, fields

def get_countries():
    """
    Returns a list of tuple of countries

    suitable for selection widget
    """
    return [
        (c.name, c.alpha2) for country in pycountry.countries.objects
    ]

class InstallCountryWizard(osv.osv_memory):
    """
    A wizard to choose a country and install its
    subdivisions
    """

    # Fields
    # ~~~~~~~
    # country: selection
    

    def install(self, cursor, user, ids, context=None):
        """
        Install the subdivisions of the country
        """
        # Read the chosen country code
        # Read the ID of the country from res.country - country_id
        # Create new subdivisions with the country as state of country_id
        # Before creating subdivision, check if it already exists
        # subdivisions = pycountry.subdivisions.get(country_code='DE')

InstallCountryWizard()
