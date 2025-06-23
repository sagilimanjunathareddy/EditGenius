import chromadb
client = chromadb.Client()

def save_to_db(doc_id, content):
    client.add(doc_id=doc_id, content=content)

def get_from_db(doc_id):
    return client.get(doc_id=doc_id)