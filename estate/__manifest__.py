{
    'name': "Real Estate",
    'version': '1.0',
    'depends': ['base'],
    'author': "Gustavo Ortega Palacios, Shet0",
    'maintainer': "Gustavo Ortega Palacios, Shet0",
    'website': 'https://gortega1211.github.io',
    'category': 'Estate',
    'description': """
    Module to bussiness case - Real Estate.
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_view.xml',
        'menus/menu.xml',
    ],
    # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'demo/demo_data.xml',
    # ],
    'license': 'LGPL-3',
    'application': True,
    'sequence': 1,
}