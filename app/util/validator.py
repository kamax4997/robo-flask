from dateutil import parser

def is_valid(date):
  format = '%Y-%m-%d %H:%M:%S'
  res = True

  try:
    res = bool(parser.parse(date))
  except ValueError:
    res = False
  return res
