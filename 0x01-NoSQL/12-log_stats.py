#!/usr/bin/env python3
"""a module for a Python script that provides
    some stats about Nginx logs stored in MongoDB"""


import pymongo
client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

value = client.logs.nginx
print(f'{value.count_documents({})} logs')
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

print('Methods:')
for method in methods:
    print(f'\tmethod {method}: {value.count_documents({"method": method})}')
print(f'{value.count_documents({"method": "GET", "path": "/status"})}\
 status check')
