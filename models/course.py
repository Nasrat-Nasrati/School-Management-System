from odoo import models, fields

class Course(models.Model):
    _name = 'school.course'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # Add this line to inherit from mail.thread
    _description = 'Course'

    name = fields.Char(string='Name', required=True)
    course_code = fields.Char(string='Course Code', required=True, unique=True)
    description = fields.Text(string='Description')
    teacher_id = fields.Many2one('school.teacher', string='Teacher')
    student_ids = fields.Many2many('school.student', string='Students')
    fees_ids = fields.One2many('school.fees', 'course_id', string='Fees')

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

