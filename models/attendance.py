from odoo import models, fields


class Attendance(models.Model):
    _name = 'school.attendance'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # Add this line to inherit from mail.thread
    _description = 'Attendance'

    student_id = fields.Many2one('school.student', string='Student', required=True)
    class_id = fields.Many2one('school.class', string='Class', required=True)
    date = fields.Date(string='Date', required=True)
    status = fields.Selection([('present', 'Present'), ('absent', 'Absent')], string='Status', required=True)
