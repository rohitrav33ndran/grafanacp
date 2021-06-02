import os
import requests

GRAFANA_TOKEN = os.environ.get('GRAFANA_TOKEN')
endpoint = "https://grafana-develop.envio.systems/api/search?folderIds=0&query=&starred=false"
headers = {"Authorization": f"Bearer {GRAFANA_TOKEN}"}

response = requests.get(endpoint,headers=headers)
j = response.content
print(j)