from odoo import api, fields, models, tools, _


class InvoiceReportWiz(models.TransientModel):
    _name = "invoice.report.wiz"
    _description = "Invocie Report Wiz"

    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')

    def check_report(self):
        inv_obj = self.env['account.move'].search([('invoice_date','>=',self.start_date),
                                                   ('invoice_date','<=',self.end_date),
                                                   ('invoice_payment_state','=','paid'),
                                                   ('state','=','posted'),
                                                   ])
        reprot =  self.env.ref('invoice_qweb_reports.report_invoice_test').report_action(inv_obj)
        return reprot
    
            