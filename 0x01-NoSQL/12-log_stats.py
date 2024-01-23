#!/usr/bin/env python3
"""
File: 12-log_stats.py

Function:
--------
A script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    count = nginx_collection.count_documents({})
    print("{} logs".format(count))

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = nginx_collection.count_documents({"method": method})
        print("\t method {}: {}".format(method, count))

    stat_count = nginx_collection.count_documents(
            {"method": "GET", "path": "/status"}
        )
    print("{} status check".format(stat_count))

