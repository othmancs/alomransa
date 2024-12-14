# -*- coding: utf-8 -*-
{
    'name': 'ZK-Biometric Device Integration',
    'version': '16.0.1.0.0',
    'category': 'Human Resources',
    'summary': "Integrating Biometric Device With HR Attendance (Face + Thumb)",
    'description': "Integrating Biometric Device With HR Attendance (Face + Thumb)",
    'author': 'Ali Hassan || HSxTech',
    'company': 'HSxTech',
    'maintainer': 'HSxTech',
    'website': "https://www.hsxtech.net",
    'depends': ['base_setup', 'hr_attendance'],
    'data': [
        'security/ir.model.access.csv',
        'data/cron.xml',
        'views/biometric_device_details_views.xml',
        'views/hr_employee_views.xml',
        'views/daily_attendance_views.xml',
        'views/biometric_device_attendance_menus.xml',
        'views/hs_shfits.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': True,
    'application': True,
    'sequence': 2,
    'images': [
        "static/description/banner.gif",
        "static/description/icon.png",
    ],
}
