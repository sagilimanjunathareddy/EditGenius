import os

def save_version(doc_id, content):
    with open(f"versions/{doc_id}.txt", 'w') as f:
        f.write(content)

def load_version(doc_id):
    with open(f"versions/{doc_id}.txt", 'r') as f:
        return f.read()
