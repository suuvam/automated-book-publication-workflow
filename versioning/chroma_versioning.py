# chroma_versioning.py
import chromadb
import os

DB_PATH = "versioning/chroma_store"

client = chromadb.PersistentClient(path=DB_PATH)
collection = client.get_or_create_collection("book_versions")

def add_version(doc_id, text, metadata=None):
    metadata = metadata or {}
    collection.add(
        documents=[text],
        ids=[doc_id],
        metadatas=[metadata]
    )
    print(f"✅ Version '{doc_id}' added.")

def get_version(doc_id):
    result = collection.get(ids=[doc_id])
    if 'documents' in result and result['documents']:
        return result['documents'][0]
    return None

def list_versions():
    all_ids = collection.get()['ids']
    return all_ids

def search_versions(query_text):
    result = collection.query(
        query_texts=[query_text],
        n_results=3
    )
    return result
