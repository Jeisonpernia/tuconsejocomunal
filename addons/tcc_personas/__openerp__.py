# -*- coding: utf-8 -*-
{
    'name': "Personas (4)",

    'summary': """
        Modulo Diseñado para la registrar personas pertenecientes al consejo comunal""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Your Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','tcc_consejo_comunales','tcc_familia'],

    # always loaded
    'data': [
        'views/personas_view.xml',
        'security/group_tcc_consejo/ir.model.access.csv',
        'security/group_tcc_residentes/ir.model.access.csv',
        'security/group_tcc_vocero/ir.model.access.csv',
        'security/filter_users_rule.xml',
    ],
}
