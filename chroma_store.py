from chromadb import PersistentClient

def save_to_chroma(url, original_text, rewritten_text):
    try:
        client = PersistentClient(path="./chroma_db")
        collection = client.get_or_create_collection("educational_content")

        collection.add(
            documents=[original_text, rewritten_text],
            metadatas=[{"type": "original", "url": url}, {"type": "rewritten", "url": url}],
            ids=[f"{url}_orig", f"{url}_rewrite"]
        )

        print("[INFO] Successfully saved to ChromaDB.")
    except Exception as e:
        print(f"[ERROR] Failed to save to ChromaDB: {e}")
