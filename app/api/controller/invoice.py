from flask import request, render_template, make_response
from flask_restplus import Resource

from app.util.dto import InvoiceDto
from app.api.service.invoice import get_all_invoices

api = InvoiceDto.api
_invoice_filter = InvoiceDto.invoices_filter
headers = {'Content-Type': 'text/html'}

@api.route('/')
class Invoices(Resource):
  @api.doc('invoices', params=_invoice_filter)
  def get(self):
    """Invoices"""
    data = {}
    args = request.args
    keys = _invoice_filter.keys()

    for key in keys:
      if args.get(key):
        data[key] = args.get(key)
    
    response = get_all_invoices(data)

    if (response.get("status") == 200):
      if (args.get("is_first") == "false"):
        return response.get("data")

      return make_response(render_template('invoice.html', invoices=response.get("data"), error_message=""), 200, headers)
    else:
      return make_response(render_template('invoice.html', invoices=[], error_message=response.get("message")), 200, headers)
