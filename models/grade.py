from odoo import models, fields

class Grade(models.Model):
    _name = 'school.grade'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # Add this line to inherit from mail.thread
    _description = 'Grade'

    student_id = fields.Many2one('school.student', string='Student', required=True)
    class_id = fields.Many2one('school.class', string='Class', required=True)
    grade = fields.Char(string='Grade', required=True)

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
