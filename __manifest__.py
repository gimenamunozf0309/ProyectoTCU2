{
    'name': 'Módulo TCU',
    'version': '1.0',
    'depends': ['base','mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/tcu_estudiante_menu.xml',
        'views/tcu_views.xml',
        'views/tcu_estudiante_views.xml',
        #'data/email_template_debug.xml',

    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,

}
