from odoo import models, fields, api, exceptions
from datetime import date

class LeaveSettlement(models.Model):
    _name = 'leave.settlement'
    _description = 'Leave Settlement'
    _inherit = 'hr.employee'

    # حقل الموظف يمكن أن يتم ربطه مباشرة بما أنك قد ورثت 'hr.employee'
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True)

    # حقل الفئات يمكن ربطه باستخدام 'related' من خلال العلاقة مع employee_id
    category_ids = fields.Many2many('hr.employee.category', related='employee_id.category_ids', string="Categories")

    iqama_number = fields.Char(string='Iqama Number', related='employee_id.iqama_number', readonly=True)
    nationality = fields.Char(string='Nationality', related='employee_id.country_id.name', readonly=True)
    joining_date = fields.Date(string='Joining Date', related='employee_id.joining_date', readonly=True)
    contract_id = fields.Many2one(
        'hr.contract',
        string="Contract",
        domain="[('employee_id', '=', employee_id)]",
        required=True
    )
    basic_salary = fields.Monetary(
        string="Basic Salary",
        related="contract_id.wage",
        readonly=True,
        currency_field="currency_id"
    )
    currency_id = fields.Many2one(
        'res.currency',
        string="Currency",
        related="contract_id.currency_id",
        readonly=True
    )

    l10n_sa_other_allowances = fields.Monetary(
        string="Other Allowances (KSA)",
        related="contract_id.l10n_sa_other_allowances",
        readonly=True,
        currency_field="currency_id"
    )
    attachment_ids = fields.Many2many(
        'ir.attachment', 'leave_settlement_attachment_rel', 'leave_settlement_id', 'attachment_id',
        string="Attachments"
    )
    last_settlement_date = fields.Date(string='Last Settlement Date')
    total_service_years = fields.Char(string='Total Service (Years & Days)', compute='_compute_service_years', store=True)
    leave_settlement_amount = fields.Float(string='Leave Settlement Amount', compute='_compute_leave_settlement', store=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], default='draft', string='Status')

    @api.depends('joining_date')
    def _compute_service_years(self):
        for record in self:
            if record.joining_date:
                delta = date.today() - record.joining_date
                years = delta.days // 365
                days = delta.days % 365
                record.total_service_years = f"{years} years and {days} days"
            else:
                record.total_service_years = 'N/A'

    @api.depends('basic_salary', 'joining_date', 'last_settlement_date')
    def _compute_leave_settlement(self):
        for record in self:
            if record.joining_date and record.basic_salary:
                delta = date.today() - record.joining_date
                years = delta.days // 365
                if years < 5:
                    record.leave_settlement_amount = (record.basic_salary / 30) * 21
                else:
                    record.leave_settlement_amount = record.basic_salary

    def action_submit(self):
        for record in self:
            if record.last_settlement_date:
                delta = date.today() - record.last_settlement_date
                if delta.days < 330:
                    raise exceptions.UserError("Cannot submit: Settlement period must be at least 330 days since last settlement.")
            record.state = 'submitted'

    def action_approve(self):
        for record in self:
            record.state = 'approved'

    def action_reject(self):
        for record in self:
            record.state = 'rejected'

    def action_reset_draft(self):
        for record in self:
            record.state = 'draft'
