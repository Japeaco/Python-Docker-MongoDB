import pymongo
import json
import urllib3
import requests
from pymongo import MongoClient
import time

connection = MongoClient('mongodb://root:example@localhost:3306')
db = connection['cadvisor']
mycol = db['normal_metrics_1']

count = 0

while count < 180:

	r = requests.get("http://localhost:808/api/v1.3/subcontainers/docker")

	conts = r.json()

	for x in conts:
		if (x.get('id') == '97073fc4ceaaace057c89cd1056caeb0f4c1ec392dc921fe0c86cf41e02c0913') or (x.get('id') == '0dc5f5c2f9b5dadf8f477888ca9d19eabf00dd5d8bd189cde42260d12acd4b45'):
  			ID = x.get('id')
			cpuusage = x.get('stats')[0].get('cpu').get('usage').get('total')
  			memoryusage = x.get('stats')[0].get('memory').get('usage')
  			iousage = x.get('stats')[0].get('network').get('memory').get('rx_bytes')
  			myposts = { "ID": ID, "CPU_Usage": cpuusage, "Memory_Usage": memoryusage, "Network_io_usage": iousage}
  			post_id = mycol.insert_one(myposts).inserted_id

	print("added successfully" + str(count))

	count += 1
	time.sleep(5)