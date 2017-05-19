# -*- coding: utf-8 -*-
{
    'name': "Gestion de Vivienda (2)",

    'summary': """
        En este modulo se relaliza el registro de las viviendas de los consejos comunales""",

    'description': """
       Este modulo es para el registro de las viviendas de los consejos comunales
    """,

    'author': "Isaac Laplante",
    'website': "http://www.yourcompany.com.ve",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','tcc_consejo_comunales'],

    # always loaded
    'data': [
        
        'views/vivienda_view.xml',
        'views/casas_view.xml',
        'views/edificios_view.xml',
        'views/callesoavenidas_view.xml',
        'views/sectores_view.xml',
        'security/ir.model.access.csv',
        'security/filter_users_rule.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
