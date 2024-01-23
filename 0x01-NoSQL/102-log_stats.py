#!/usr/bin/env python3
"""
File: 102-log_stats.py

Function:
--------
- A script that provides some stats about Nginx logs stored in MongoDB
- Adds the top 10 of the most present IPs in the collection nginx od the
database logs.
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
        print("\tmethod {}: {}".format(method, count))

    stat_count = nginx_collection.count_documents(
            {"method": "GET", "path": "/status"}
        )
    print("{} status check".format(stat_count))

    print("IPs:")
    result = nginx_collection.aggregate([
        {
            "$group": {
                "_id": "$ip",
                "count": {"$sum": 1}
                }
        },
        {
            "$sort": {
                "count": -1
                }
        },
        {
            "$limit": 10
        },
    ])
    for doc in result:
        print(f"\t{doc['_id']}: {doc['count']}")

