#faiss_utils.py
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from constants import emergency_responses  

index = None
model = SentenceTransformer('all-MiniLM-L6-v2')

def initialize_faiss():
    global index
    emergency_keys = list(emergency_responses.keys())
    embeddings = model.encode(emergency_keys)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings, dtype='float32'))
    print("FAISS index initialized.")

def find_closest_emergency(query):
    embedding = model.encode([query])
    D, I = index.search(np.array(embedding, dtype='float32'), k=1)
    closest_emergency = list(emergency_responses.keys())[I[0][0]]
    distance = D[0][0]
    return closest_emergency, distance
