#!/usr/bin/env python3
"""a module for a Python script that provides
    some stats about Nginx logs stored in MongoDB"""

if __name__ == "__main__":
    import pymongo
    from collections import Counter

    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

    val = client.logs.nginx
    print(f'{val.count_documents({})} logs')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print('Methods:')
    for method in methods:
        print(f'\tmethod {method}: {val.count_documents({"method": method})}')
    print(f'{val.count_documents({"method": "GET", "path": "/status"})}\
 status check')
    print('IPs:')
    my_values = val.find()
    ips = [item.get('ip') for item in my_values]
    res = Counter(ips)
    result = res.most_common()
    for ip in result[:10]:
        print(f'\t{ip[0]}: {ip[1]}')
