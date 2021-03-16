#!/usr/bin/env python3
"""
102-log_stats.py
Module for using PyMongo to parse nginx logs
"""

from pymongo import MongoClient

if __name__ == "__main__":
    """
    Provides some stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://localhost')
    nginx_collection = client.logs.nginx
    n_logs = nginx_collection.count_documents({})
    print(f'{n_logs} logs')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f'{status_check} status check')
