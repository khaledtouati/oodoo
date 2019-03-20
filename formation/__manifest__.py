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
    'depends': ['base', 'mail'],
    'summary': 'summary1, summary2, ',
    'data': [
        #'security/ModuleName.xml',
        #'security/ir.model.access.csv',
        #'data/ModuleName_data.xml',
        'views/formation_views.xml',
        'menu.xml',
    ],
    'demo': [
        #'demo/ModuleName_demo.xml'
    ],
    'css': [
        #'static/src/css/ModuleName_style.css'
    ],
    
    'price': 100.00,
    'currency': 'EUR',
    'installable': True,
    'application': True,
}
