from odoo import models, fields

class Teacher(models.Model):
    _name = 'school.teacher'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # Add this line to inherit from mail.thread
    _description = 'Teacher'

    name = fields.Char(string='Name', required=True)
    teacher_id = fields.Char(string='Teacher ID', required=True, unique=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Text(string='Address')
    course_ids = fields.One2many('school.course', 'teacher_id', string='Courses')

    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('confirm', 'Confirm'),
            ('approve', 'Approve'),
            ('done', 'Done')
        ],
        string='Status',
        default='draft',
        tracking=True
    )

