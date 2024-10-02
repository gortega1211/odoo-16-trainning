{
    'name': "Real Estate",
    'version': '1.0',
    'depends': ['base'],
    'author': "Gustavo Ortega Palacios, Shet0",
    'category': 'Estate',
    'description': """
    Module Real Estate
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_view.xml',
        'views/estate_property_type_view.xml',
        'views/estate_property_tag_view.xml',
        'views/estate_property_offer_view.xml',
        'menus/menu.xml',
    ],
    # data files containing optionally loaded demonstration data
    #'demo': [
    #    'demo/demo_data.xml',
    #],
    'license': 'LGPL-3',
    'application': True,
    'sequence': 1,
}