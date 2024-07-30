{
    'name': 'School Management System',
    'version': '17.0.0.1',
    'sequence': 1,
    'summary': 'Manage school operations including students, teachers, courses, classes, attendance, and grades.',
    'description': """
School Management System
========================
This module helps manage the various aspects of a school, including:
- Student Information
- Teacher Information
- Courses
- Classes
- Attendance Tracking
- Grading System
""",
    'author': 'Nasrat Nasrati',
    'website': 'https://www.yourwebsite.com',
    'category': 'Education',
    'depends': ['base', 'mail'],
    'data': [

        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/student.xml',
        'views/teacher.xml',
        'views/class.xml',
        'views/course.xml',
        'views/grade.xml',
        'views/attendance.xml',
        'views/student_fess.xml',
        'data/user_default_data.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',

    'qweb': [
        'static/src/xml/user_menu.xml',

    ],
    'assets': {
        'web.assets_backend': [
            'SMS/static/src/js/extended_user_menu.js',


        ],
    }
}
