#!/usr/bin/env python3
"""
Script to provide statistics about Nginx logs stored in MongoDB.
"""

import pymongo

def get_nginx_logs_stats():
    # Connect to MongoDB and get the 'logs' database and 'nginx' collection
    client = pymongo.MongoClient()
    db = client.logs
    collection = db.nginx

    # Get the total number of documents in the collection
    total_logs = collection.count_documents({})

    # Get the number of documents with each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in methods}

    # Get the number of documents with method=GET and path=/status
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})

    return total_logs, method_counts, status_check_count

def display_stats(total_logs, method_counts, status_check_count):
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}:", count)
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    total_logs, method_counts, status_check_count = get_nginx_logs_stats()
    display_stats(total_logs, method_counts, status_check_count)
