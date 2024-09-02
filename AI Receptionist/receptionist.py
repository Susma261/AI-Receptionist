import streamlit as st
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import time
from transformers import pipeline

# Initialize FAISS index
index = None

# Initialize SentenceTransformer model for embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize Hugging Face GPT-2 for text generation
generator = pipeline('text-generation', model='gpt2')

# Emergency data for FAISS with only first aid information
emergency_responses = {
    "not breathing": "1. Call emergency services immediately. 2. Start CPR (Cardiopulmonary Resuscitation). Place the person on a firm surface, kneel beside them, place your hands one on top of the other on their chest, and push hard and fast (about 100-120 compressions per minute). 3. Continue CPR until emergency services arrive or the person starts breathing.",
    "chest pain": "1. Sit or lie down in a comfortable position. 2. Chew and swallow an aspirin (if not allergic and if advised by a healthcare professional). 3. Call emergency services immediately. 4. Keep calm and avoid any physical activity until help arrives.",
    "bleeding": "1. Apply direct pressure to the wound using a clean cloth or bandage. 2. If possible, elevate the injured area above the level of the heart. 3. Continue applying pressure until help arrives or the bleeding stops.",
    "burn": "1. Cool the burn under running cold water for at least 10 minutes. 2. Cover the burn with a clean, non-stick bandage. 3. Avoid applying ice or butter. 4. Seek medical attention if the burn is severe or covers a large area.",
    "choking": "1. Encourage the person to cough if they can. 2. If the person cannot cough, perform abdominal thrusts (Heimlich maneuver). Stand behind the person, place your arms around their waist, make a fist with one hand, and place it just above their navel. Grasp your fist with the other hand and perform quick, inward and upward thrusts. 3. Continue until the object is expelled or the person starts breathing."
}

# Function to initialize FAISS index
def initialize_faiss():
    global index
    emergency_keys = list(emergency_responses.keys())
    embeddings = model.encode(emergency_keys)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings, dtype='float32'))
    print("FAISS index initialized.")

initialize_faiss()

# Function to find closest emergency
def find_closest_emergency(query):
    embedding = model.encode([query])
    D, I = index.search(np.array(embedding, dtype='float32'), k=1)
    closest_emergency = list(emergency_responses.keys())[I[0][0]]
    distance = D[0][0]
    return closest_emergency, distance

# Function to get LLM response
def get_llm_response(prompt):
    response = generator(prompt, max_length=100, num_return_sequences=1)
    return response[0]['generated_text'].strip()

# Streamlit app interface
st.title("Dr.Ardin's AI Receptionist")

# User input
user_input = st.text_input("Are you experiencing an emergency or would you like to leave a message?")

if user_input:
    if "emergency" in user_input.lower():
        st.write("What is your emergency?")
        emergency_input = st.text_input("Describe your emergency:")
        
        if emergency_input:
            closest_emergency, distance = find_closest_emergency(emergency_input)
            
            with st.spinner("Checking the database for guidance..."):
                time.sleep(15)  # Simulating delay for guidance retrieval
            
            # Use GPT-2 to generate additional guidance
            llm_prompt = f"Provide first aid guidance for the situation: {emergency_input}"
            additional_guidance = get_llm_response(llm_prompt)
            
            st.write(f"Guidance found for: {closest_emergency}")
            st.write(emergency_responses[closest_emergency])
            st.write(f"Additional guidance from GPT-2: {additional_guidance}")
            
            user_location = st.text_input("Meanwhile, can you tell me which area you are located in right now?")
            
            if user_location:
                st.write(f"Dr. Adrin will be coming to your location in approximately {np.random.randint(5, 15)} minutes.")
                st.write("Please follow the steps while you wait.")
    else:
        st.write("Please provide your message:")
        message = st.text_area("Enter your message:")
        
        if message:
            st.write("Thanks for the message, we will forward it to Dr. Adrin.")
