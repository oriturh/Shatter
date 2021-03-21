#  ----- RUN THIS FIRST -----
import django_setup_script
#  --------------------------

from django.conf import settings

# if not hasattr(settings, 'OPENSEA_API_KEY'):
#     raise ValueError("OPENSEA_API_KEY not found in local_settings")

# OPENSEA_API_KEY = settings.OPENSEA_API_KEY

if not hasattr(settings, 'ETH_ADDRESS_LIST'):
    raise ValueError("ETH_ADDRESS_LIST not found in local_settings")

ETH_ADDRESS_LIST = settings.ETH_ADDRESS_LIST

OPENSEA_API_URL = settings.OPENSEA_API_URL

if hasattr(settings, 'OPENSEA_API_KEY'):
    OPENSEA_API_KEY = settings.OPENSEA_API_KEY
else:
    OPENSEA_API_KEY = ""

import json
import requests

addressIndex = 0

url = "https://api.opensea.io/api/v1/assets" + "?X-API-KEY=" + OPENSEA_API_KEY
querystring = {
    "owner":ETH_ADDRESS_LIST[addressIndex],
    "order_direction":"desc",
    "offset":"0",
    "limit":"20"
    }

print("Querying Opensea =>")
print("URL: " + url)
print("Address: " + ETH_ADDRESS_LIST[addressIndex])
response = requests.request("GET", url, params=querystring)

dumpFile = "scripts_dump.txt"
print("Writing response to =>", dumpFile)

with open(dumpFile, "w") as f:
    f.write("URL: " + url + '\n')
    f.write("Address: " + ETH_ADDRESS_LIST[addressIndex] + '\n')
    respJSON = response.json()
    for key in respJSON:
        itemCount = 1
        f.write("Key: -----> " + key + '\n')   
        for item in respJSON[key]:
            f.write("-"*20 + ' ' + str(itemCount) + ' ' + "-"*20 + '\n')
            f.write(json.dumps(item, indent = 4) + '\n')
            itemCount += 1
print("Done")



