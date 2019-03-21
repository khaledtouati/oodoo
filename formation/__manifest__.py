# -*- coding: utf-8 -*-

{
    'name': 'new mod',
    'version': '1.0',
    'author': 'Ait-Mlouk Addi',
    'website': 'https://www.sdatacave.com',
    'support': 'aitmlouk@gmail.com',
    'license': "AGPL-3",
    'complexity': 'easy',
    'sequence': 1,
    'category': 'category',
    'description': """
        Put your description here for your module:
            - model1
            - model2
            - model3
    """,
    'depends': ['base','mail','hr','website'],
    'summary': 'summary1, summary2, ',
    'data': [
        #'security/ModuleName.xml',
        #'security/ir.model.access.csv',
        #'data/ModuleName_data.xml',
       
        'security/formation.xml',
        'security/ir.model.access.csv',
       
        'views/formation_views.xml',
       'views/formation_inherit.xml',
       'data/sequence.xml',
        'demo/demo.xml' ,
       'wizard/wiz_views.xml',
        'report/report.xml',
        'report/registration.xml',

        'menu.xml',
    ],
    'demo': [
        'demo/demo.xml'
    ],
    'css': [
        #'static/src/css/ModuleName_style.css'
    ],
    
    'price': 100.00,
    'currency': 'EUR',
    'installable': True,
    'application': True,
}
