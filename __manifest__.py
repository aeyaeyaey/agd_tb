{
    'name': 'agd',
    'version': '1.0',
    'category': 'Uncategorized',
    'summary': 'AGD Management Module',
    'description': """
    Custom module for managing AGD.
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/birim_views.xml',
        'views/signup_template.xml',
        'data/il_ilce_data.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'agd/static/src/js/signup.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}