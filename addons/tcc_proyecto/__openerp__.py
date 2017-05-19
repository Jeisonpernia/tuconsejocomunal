# -*- coding: utf-8 -*-
{
    'name': "Gestion de proyecto (6)",

    'summary': """
        """,

    'description': """
        
    """,

    'author': "Yorgenis, Wladimir",
    

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'proyecto',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','project','tcc_consejo_comunales'],

    # always loaded
    'data': [
        'views/tcc_proyecto.xml',
        'security/group_tcc_consejo/ir.model.access.csv',
        'security/group_tcc_residentes/ir.model.access.csv',
        'security/group_tcc_vocero/ir.model.access.csv',
        'security/filter_users_rule.xml',
         
         
    ],
    # only loaded in demonstration mode
    'demo': [
       # 'demo.xml',
    ],
}
