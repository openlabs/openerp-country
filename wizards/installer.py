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

COUNTRIES_LIST = [(c.alpha2, c.name) for c in pycountry.countries.objects]

class InstallCountryWizard(osv.osv_memory):
    """
    A wizard to choose a country and install its
    subdivisions
    """
    _name = 'country.subdivision_wizard'
    _description = "Install Country"
    
    _columns = {
        'country': fields.selection(
            COUNTRIES_LIST, 
            'Country', 
            required=True
        )
    }    

    def install(self, cursor, user, ids, context=None):
        """
        Install the subdivisions of the country
        
        :param cursor: Database Cursor
        :param user: ID of current user
        :param ids: ID of current record.
        :param context: Context from parent method(no direct use)
        
        :return: ir.actions.act_window_close for closing
        """
        country_obj = self.pool.get('res.country')
        state_obj = self.pool.get('res.country.state')
        for country in self.browse(cursor, user, ids, context):
            country_code = country.country
            country_id = country_obj.name_search(cursor, user, 
                                                 name=country_code, 
                                                 context=context)[0][0]
            states = pycountry.subdivisions.get(country_code=country_code)
            for subdivisions in states:
                existing_subdivisions = state_obj.search(
                                         cursor, 
                                         user, 
                                         [('name', '=', subdivisions.name)], 
                                         context=context,
                )
                if not existing_subdivisions:
                    vals = {
                        'country_id': country_id,
                        'name': subdivisions.name,
                        'code': subdivisions.code
                            }
                    state_obj.create(cursor, user, vals, context)
            return {'type':'ir.actions.act_window_close' }

InstallCountryWizard()
