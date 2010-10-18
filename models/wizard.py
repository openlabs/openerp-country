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

def get_countries(klass, cursor, user, context=None):
    """
    Returns a list of tuple of countries
    Each tuple contains the Country Name and Code
    e.g. - ('India', 'IN')

    suitable for selection widget
    """
    return [
        (country.alpha2, country.name) \
            for country in pycountry.countries.objects
    ]

class InstallCountryWizard(osv.osv_memory):
    """
    A wizard to choose a country and install its
    subdivisions
    """
    _name = 'install.country.wizard'
    _description = "Install Country"
    
    _columns = {
        'country': fields.selection(
            get_countries, 
            'Country', 
            required=True
        )
    }    

    def install(self, cursor, user, ids, context=None):
        """
        Install the subdivisions of the country
        """
        country_obj = self.pool.get('res.country')
        state_obj = self.pool.get('res.country.state')
        if ids:
            country_code = self.browse(cursor, user, ids[0], context).country
            country_id = country_obj.name_search(cursor, user, 
                                                 name=country_code, 
                                                 context=context)[0][0]
            states = pycountry.subdivisions.get(country_code=country_code)
            for state in states:
                conflicting_state = state_obj.search(cursor, user, 
                                                  [('name', '=', state.name)], 
                                                  context=context)
                if not conflicting_state:
                    vals = {
                        'country_id': country_id,
                        'name': state.name,
                        'code': state.code
                            }
                    state_obj.create(cursor, user, vals, context)
            return {'type':'ir.actions.act_window_close' }

InstallCountryWizard()
