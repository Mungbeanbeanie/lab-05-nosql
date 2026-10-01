#!/usr/bin/env python3

import os

import logging

from pymongo import MongoClient
from pymongo.errors import PyMongoError

MONGODB_ATLAS_URL = os.environ.get("MONGODB_ATLAS_URL")
MONGODB_ATLAS_USER = os.environ.get("MONGODB_ATLAS_USER")
MONGODB_ATLAS_PWD = os.environ.get("MONGODB_ATLAS_PWD")

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def main():
    '''Connects to MongoDB Atlas and prints the total number of
    authors from the list of _id values in the bookstore db
    and the authors and books collections.'''

    client = None
    try:
        #connect to MongoDB Atlas
        client = MongoClient(MONGODB_ATLAS_URL, username=MONGODB_ATLAS_USER, password=MONGODB_ATLAS_PWD)
        client.admin.command("ping")  # force a connection so errors show up here
        logging.info("Connected to MongoDB Atlas")

        #select the bookstore db and authors and books collections
        db = client.bookstore
        authors_collection = db.authors
        books_collection = db.books

        #list of author _id values
        author_ids = ["author_001", "author_002", "author_003", "author_004"]

        #prints numbers of authors and name, book title, and publication year
        total = authors_collection.count_documents({"_id": {"$in": author_ids}})
        print(f"Authors: {total}")

        for author in authors_collection.find({"_id": {"$in": author_ids}}):
            print(f"\n{author['name']}")
            # join: books whose author_ids array contains this author's _id
            for book in books_collection.find({"author_ids": author["_id"]}):
                print(f"  {book['title']} ({book['published_year']})")
    except PyMongoError as e:
        logging.error("MongoDB error: %s", e)
    finally:
        if client is not None:
            client.close()
            logging.info("Connection closed")

if __name__ == "__main__":
    main()
