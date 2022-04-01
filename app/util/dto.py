from importlib.resources import path
from flask_restplus import Namespace, fields


class InvoiceDto:
  api = Namespace('Invoice', description='Operations related to invoice', path='/invoices')
  invoice = api.model('invoice', {
    'state': fields.String(required=True, description='Invoice status'),
    'number': fields.String(required=True, description='Full invoice number'),
    'date_invoice': fields.String(required=True, description='Invoice date'),
    'date_due': fields.String(required=True, description='Invoice due date'),
    'currency': fields.String(required=True, description='Invoice currency ISO code, e,g. "EUR"', len=3),
    'partner_name': fields.String(required=True, description='Partner name'),
  })

  invoices_params = api.model('invoice filter', {
    'secret': fields.String(required=True, description='Identification, unique number provided by RoboLabs'),
    'date_from': fields.String(required=True, description='Invoice creation/modification date range start, format YYYY-MM-DD HH:MM:SS; either creation/modification or invoice date range should be provided'),
    'date_to': fields.String(required=True, description='Invoice creation/modification date range end, format YYYY-MM-DD HH:MM:SS; either creation/modification or invoice date range should be provided'),
    'data_type': fields.String(required=False, description='Indication, what date range should be used, possible values:  „create“ - invoices are created in specified  ate range  „modify“ - invoices are updated in specified date range Data type is set to „create“ by default'),
    'invoice_date_from': fields.String(required=True, description='Invoice date range start, format YYYY-MM-DD; either creation/modification or invoice date range should be provided'),
    'invoice_date_to': fields.String(required=True, description='Invoice date range end, format YYYY-MM-DD; either creation/modification or invoice date range should be  provided'),
  })

  invoice_params = api.model('invoices filter', {
    'secret': fields.String(required=True, description='Identification, unique number provided by RoboLabs'),
    'invoice_id': fields.Integer(required=True, description='Invoice identificator; it is required to specify invoice identificator or invoice number or invoice comment or invoice reference with partner code'),
    'invoice_number': fields.String(required=True, description='Invoice number; it is required to specify invoice identificator or invoice number or invoice comment or invoice reference with partner code'),
    'invoice_reference': fields.String(required=True, description='Invoice reference provided by supplier; it is required to specify invoice identificator or invoice number or invoice comment or invoice reference with partner code'),
    'partner_code': fields.String(required=True, description='Invoice partner code; required when invoice reference is specified'),
    'comment': fields.String(required=True, description='Additional invoice information; it is required to specify invoice identificator or invoice number or invoice comment or invoice reference with partner code'),
    'comment': fields.Boolean(required=False, description='Indication, if a PDF copy of invoice encoded in base64 format should be provided'),
  })

  invoices_filter = {
    'secret': 'Identification, unique number provided by RoboLabs',
    'date_from': 'Invoice creation/modification date range start, format YYYY-MM-DD HH:MM:SS; either creation/modification or invoice date range should be provided',
    'date_to': 'Invoice creation/modification date range end, format YYYY-MM-DD HH:MM:SS; either creation/modification or invoice date range should be provided',
    'data_type': 'Indication, what date range should be used, possible values:  „create“ - invoices are created in specified  ate range  „modify“ - invoices are updated in specified date range Data type is set to „create“ by default',
    'invoice_date_from': 'Invoice date range start, format YYYY-MM-DD; either creation/modification or invoice date range should be provided',
    'invoice_date_to': 'Invoice date range end, format YYYY-MM-DD; either creation/modification or invoice date range should be  provided',
  }
