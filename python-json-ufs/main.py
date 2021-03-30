import urllib.request  
import json

url = 'https://sisu-api-pcr.apps.mec.gov.br/api/v1/oferta/instituicoes'
resp = urllib.request.urlopen(url+str()).read()
resp = json.loads(resp.decode('utf-8'))

for x in resp:  
   print(x['co_ies']+' - '+x['no_ies'])
   print("")