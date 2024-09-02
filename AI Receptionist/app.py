import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
import numpy as np
import time
import random

# Initialize model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Initialize Qdrant client
qdrant_client = QdrantClient(host='localhost', port=6333)
collection_name = 'receptionist'
dimension = 768  # Dimension for GPT-2 embeddings (set to 768 for BERT-like models)

# Create collection if it doesn't exist
try:
    qdrant_client.create_collection(
        collection_name=collection_name,
        vector_size=dimension,
        distance='Cosine'
    )
except Exception as e:
    print("Collection already exists or an error occurred:", e)

def get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=1)
    embedding = outputs[0].detach().numpy().flatten()
    return embedding

def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=150, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def handle_user_input(user_input, state):
    user_input = user_input.strip().lower()

    if state == 'initial':
        if 'emergency' in user_input:
            state = 'emergency'
            return "Please specify the nature of your emergency:", state
        elif 'message' in user_input:
            state = 'message'
            return "Please provide your message for Dr. Adrin:", state
        else:
            return "I didn’t understand that. Are you experiencing an emergency or would you like to leave a message?", state

    elif state == 'message':
        # Store message in Qdrant
        embedding = get_embedding(user_input)
        point_id = len(qdrant_client.scroll(collection_name)[0]) + 1  # Generate a new ID
        point = PointStruct(id=point_id, vector=embedding.tolist())
        qdrant_client.upsert(collection_name=collection_name, points=[point])
        return "Thank you for your message. Dr. Adrin will review it shortly.", 'initial'
    
    elif state == 'emergency':
        # Artificial delay for database simulation
        time.sleep(15)  # Simulate delay for emergency handling
        if 'not breathing' in user_input:
            guidance = "perform CPR immediately. Push hard and fast on the center of the chest, at a rate of 100-120 compressions per minute. Seek guidance immediately if unsure."
            next_step = f"Please {guidance} Meanwhile, could you tell me your current location?"
            state = 'location'
        else:
            guidance = "follow standard emergency procedures while Dr. Adrin is on the way."
            next_step = f"Please {guidance} Meanwhile, could you tell me your current location?"
            state = 'location'
        return next_step, state

    elif state == 'location':
        eta = random.randint(5, 30)
        return f"Dr. Adrin is on the way to your location. Estimated time of arrival is {eta} minutes. Please follow the provided steps in the meantime.", 'initial'

    return "I’m not sure what you mean. Could you clarify if you’re experiencing an emergency or want to leave a message?", state

def main():
    st.set_page_config(page_title="AI Receptionist", page_icon=":speech_balloon:", layout="wide")

    st.title("AI Receptionist for Dr. Adrin")

    # Initialize session state
    if 'state' not in st.session_state:
        st.session_state.state = 'initial'
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""

    # Display chat history
    st.markdown('<div class="chat-box">', unsafe_allow_html=True)
    for message in reversed(st.session_state.chat_history):
        if message['role'] == 'User':
            st.markdown(f"<div class='user-message'>{message['text']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='ai-message'>{message['text']}</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Form for user input
    form = st.form(key='user_input_form')
    user_input = form.text_input("Type your message here...", key='text_input')
    submit_button = form.form_submit_button("Send")

    if submit_button:
        if user_input:
            st.session_state.chat_history.append({'role': 'User', 'text': user_input})
            
            # Handle the input and update the state
            response, st.session_state.state = handle_user_input(user_input, st.session_state.state)
            st.session_state.chat_history.append({'role': 'AI', 'text': response})
            
            # Clear the input field by updating session state
            st.session_state.user_input = ""
            
            # Scroll to the bottom
            st.markdown("""
                <script>
                var chatBox = document.querySelector('.chat-box');
                chatBox.scrollTop = chatBox.scrollHeight;
                </script>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
