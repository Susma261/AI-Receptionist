# AI-Receptionist for Doctor: 
AI_Receptionist/


├── ai_receptionist.py       
├── faiss_utils.py           
├── text_generation.py     
├── session_state.py         
├── styles.py                
├── constants.py                   
└── requirements.txt

This project is an AI-powered text-based receptionist system for a doctor, which assists in handling emergencies and messages. It uses machine learning and natural language processing (NLP) techniques to identify the type of query (emergency or message), fetch appropriate emergency responses from a vector database (FAISS), and manage conversation states using Streamlit.

## Features
Emergency Handling: Provides immediate guidance on emergencies based on predefined scenarios.
Message Handling: Allows users to leave messages that are forwarded to the doctor.
Natural Language Processing: Uses LLMs (GPT-2) to generate responses.
Vector Database Integration: Utilizes FAISS for efficient similarity search to match emergencies.
Asynchronous Processing: Implements delayed responses to simulate real-time data retrieval.
