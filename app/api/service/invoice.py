import json
from pickle import TRUE
import requests
import os

from app.util.validator import is_valid

base_api_url = os.environ.get('API_URL')
secret_key = os.environ.get('API_KEY')

headers = {
  'Content-Type': 'application/json',
  'x-api-key': secret_key
}

def get_all_invoices(request):
  api_url = f'{base_api_url}/api/get_invoice_list'

  if request is not None:
    request['execute_immediately'] = 'true'
    
  try:
    result = requests.post(api_url, data=json.dumps(request), headers=headers)
  except Exception as e:
    response = {
      'status': 'error',
      'message': 'Something went wrong!'
    }
    return response

  response = {
    'status': result.json()['result']['status_code'],
    'data': result.json()['result']['data']
  }
  
  return response
