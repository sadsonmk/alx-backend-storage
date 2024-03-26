#!/usr/bin/env python3
"""a module for a Python script that provides
    some stats about Nginx logs stored in MongoDB"""

if __name__ == "__main__":
    import pymongo
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

    val = client.logs.nginx
    print(f'{val.count_documents({})} logs')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print('Methods:')
    for method in methods:
        print(f'\tmethod {method}: {val.count_documents({"method": method})}')
    print(f'{val.count_documents({"method": "GET", "path": "/status"})}\
 status check')
