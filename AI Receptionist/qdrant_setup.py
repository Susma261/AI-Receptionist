from qdrant_client import QdrantClient

# Initialize Qdrant client
client = QdrantClient(host="localhost", port=6333)

# Create a collection
client.recreate_collection(
    collection_name="emergency_responses",
    vector_size=10  # Size of your vector space; should match your vector dimensions
)

# Add emergency responses
data = [
    {
        "id": "1",
        "payload": {
            "description": "Not breathing",
            "guidance": "Perform CPR immediately. Push hard and fast in the center of the chest at a rate of 100-120 compressions per minute."
        }
    },
    {
        "id": "2",
        "payload": {
            "description": "Heart attack",
            "guidance": "Call emergency services immediately. If the person is conscious, have them chew and swallow aspirin. If unconscious, perform CPR."
        }
    },
    {
        "id": "3",
        "payload": {
            "description": "Severe bleeding",
            "guidance": "Apply pressure to the wound to stop the bleeding. Elevate the injured area if possible. Seek emergency medical help."
        }
    }
]

# Insert data into collection
client.upsert(
    collection_name="emergency_responses",
    points=data
)
