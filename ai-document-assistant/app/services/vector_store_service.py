import uuid
import chromadb

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection(name="docs")


def store_chunks(file_name: str, chunks: list[str]) -> int:
    ids = []
    metadatas = []
    docs = []

    for index, chunk in enumerate(chunks):
        ids.append(str(uuid.uuid4()))
        docs.append(chunk)
        metadatas.append({
            "file_name": file_name,
            "chunk_index": index
        })

    if docs:
        collection.add(
            ids=ids,
            documents=docs,
            metadatas=metadatas
        )

    return len(docs)

def search_relevant_chunks(question: str, max_results: int = 3) -> list[dict]:
    results = collection.query(
        query_texts=[question],
        n_results=max_results
    )

    matches = []

    docs = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    for i, document in enumerate(docs):
        matches.append({
            "text": document,
            "metadata": metadatas[i],
            "distance": distances[i]
        })

    return matches