import requests

url_prefix = 'https://cellapi.de.tesla.com/v1/prd/trays/'
url_postfix = '/clear_all_cells'

trays = ['CF:S101002342:ZC',
         'CF:S101015178:ZC',
         'CF:S101019065:ZA',
         'CF:S101018753:ZA',
         'CF:S101002010:ZC',
         'CF:S101019117:ZC',
         'CF:S101000212:ZC',
         'CF:S101016244:ZA']

body_json = '{"equipment_name": "GFBB-CM1-FMA1-50401"}'
# in order to add location  use body_json in request.post method

for tray in trays:
    url = url_prefix + tray + url_postfix
    # Create a new resource
    response = requests.post(url, verify=False)
    print(response)
