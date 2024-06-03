{
    'name': 'agd',
    'version': '1.0',
    'category': 'Uncategorized',
    'summary': 'AGD Management Module',
    'description': """
    Custom module for managing AGD.
    """,
    'depends': ['base', 'auth_signup', 'website_profile'],
    'data': [
        'security/ir.model.access.csv',
        'security/ir.rule.xml',
        'views/birim_views.xml',
        'views/signup_template.xml',
        'views/templates.xml',
        'views/res_users_views.xml',
        'data/il_ilce_data.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'agd/static/src/js/signup.js',
            'agd/static/src/js/profile_edit.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}