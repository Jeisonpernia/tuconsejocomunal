# -*- coding: utf-8 -*-
{
    'name': "Encuestas de Consejos Comunales (5)",

    'summary': """
        Registro de encuestas realizadas a consejos comunales""",

    'description': """
        Se realizan las encuestas a diferentes consejos comunales
    """,

    'author': "Angela Mercedes Rangel,Andrea Parra, Lanrys Gil ",
    

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Encuestas',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','survey','tcc_consejo_comunales'],

    # always loaded
    'data': [
        'views/survey_survey.xml',
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
