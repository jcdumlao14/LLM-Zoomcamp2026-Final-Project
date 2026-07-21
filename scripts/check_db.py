import chromadb

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection("medical_papers")

print("=" * 50)
print("MedRAG AI")
print("Vector Database Check")
print("=" * 50)

print(f"Collection Name : {collection.name}")
print(f"Total Documents : {collection.count()}")