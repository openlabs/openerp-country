#:copyright: (c) 2010 by Openlabs Technologies & Consulting (P) LTD.
#:license: AGPL, see LICENSE for more details
{
    'name' : 'Country',
    'version' : '0.1',
    'depends' : [
                'base',
                ],
    'author' : 'Openlabs Technologies & Consulting (P) LTD',
    'description': '''
    Install additional countries and subdivisions.
    
    Note : Requires pycountry module. Use easy_install

    Inspired by Tryton (http://tryton.org)
    ''',
    'website' : 'http://openlabs.co.in/',
    'category' : 'Generic Modules',
    'init_xml' : [ ],
    'demo_xml' : [ ],
    'update_xml' : [
        'views/view.xml',
    ],
    'active': False,
    'installable': True,
}

