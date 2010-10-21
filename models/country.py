'''
    Customizing country.state to increase the length of state code to 5.

    :copyright: (c) 2010 by Openlabs technologies & Consulting (P) LTD
    :license: AGPL, see LICENSE for more details
'''
from osv import osv, fields

class CountryState(osv.osv):
    """
    Inherit Country.State and create a field for State Code 
    """
    _inherit = 'res.country.state'
    
    _columns = {
        'code': fields.char('State Code', size=5,
            help='The state code in five chars.\n', required=True),
    }

CountryState()