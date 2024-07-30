from odoo import models, fields


class Student(models.Model):
    _name = 'school.student'
    _inherit = ['mail.thread']
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    student_id = fields.Char(string='Student ID', required=True, unique=True)
    date_of_birth = fields.Date(string='Date of Birth')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Text(string='Address')
    courses_ids = fields.Many2many('school.course', string='Courses')
    fees_ids = fields.One2many('school.fees', 'student_id', string='Fees')

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


    # These fields are automatically added by mail.thread
    message_ids = fields.One2many('mail.message', 'res_id', string='Messages', readonly=True, copy=False)
    message_follower_ids = fields.Many2many('res.partner', 'mail_followers_rel', 'res_id', 'partner_id',
                                            string='Followers', readonly=True, copy=False)
    activity_ids = fields.One2many('mail.activity', 'res_id', string='Activities', readonly=True, copy=False)
    message_attachment_count = fields.Integer(string='Attachment Count', compute='_compute_message_attachment_count',
                                              readonly=True)
