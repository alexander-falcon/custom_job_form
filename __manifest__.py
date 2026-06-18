# -*- coding: utf-8 -*-

{
    'name': "Personalización de Solicitud de Trabajo",
    'version': '16.0.1.0.0',
    'category': 'Human Resources/Recruitment',
    'summary': 'Modifica el formulario de solicitud de trabajo',
    'description': """
        Este módulo personaliza el formulario de solicitud de trabajo
        cambiando el título de la página y ocultando campos específicos.
    """,
    'depends': ['hr_recruitment'],
    'data': [
        'security/ir.model.access.csv',
        'views/website_hr_recruitment_templates.xml',
    ],
    'qweb': [],
    'demo': [],
    'installable': True,
    'application': False,
    'author': "Alexander Falcon",
    # 'website': "http://www.yourcompany.com",
    'license': 'LGPL-3',
}
