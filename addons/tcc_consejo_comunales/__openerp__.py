# -*- coding: utf-8 -*-
{
    'name': "Gestión de los Consejos Comunales (1)",

    'summary': """ En este módulo se registra a los Consejos Comunales""",

    'description': """
        Registro de los Consejos Comunales 
    """,

    'author': "Felipe Villamizar",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','usuarios_venezuela','survey','project'],

    # always loaded
    'data': [
        'views/consejocomunal_views.xml',
        'security/group_tcc_consejo/ir.model.access.csv',
        'security/group_tcc_residentes/ir.model.access.csv',
        'security/group_tcc_vocero/ir.model.access.csv',
        'security/filter_users_rule.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
