# AI-Receptionist for Doctor: 
AI_Receptionist/


├── ai_receptionist.py       
├── faiss_utils.py           
├── text_generation.py     
├── session_state.py         
├── styles.py                
├── constants.py                   
└── requirements.txt

## Introduction
This project is an AI-powered text-based receptionist system for a doctor, which assists in handling emergencies and messages. It uses machine learning and natural language processing (NLP) techniques to identify the type of query (emergency or message), fetch appropriate emergency responses from a vector database (FAISS), and manage conversation states using Streamlit.

## Features
Emergency Handling: Provides immediate guidance on emergencies based on predefined scenarios.
Message Handling: Allows users to leave messages that are forwarded to the doctor.
Natural Language Processing: Uses LLMs (GPT-2) to generate responses.
Vector Database Integration: Utilizes FAISS for efficient similarity search to match emergencies.
Asynchronous Processing: Implements delayed responses to simulate real-time data retrieval.

## Project Setup
1. Clone the repository:
   git clone <repository-url>
   cd AI_Receptionist

2. Create and activate a virtual environment:
  python -m venv venv
  source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Run the Streamlit app:
   streamlit run ai_receptionist.py
## File Descriptions

### ai_receptionist.py: 
The main file for running the Streamlit app. It handles user interactions, manages session states, and integrates emergency handling and messaging functionality. It utilizes functions from other scripts to perform tasks like checking user inactivity, interacting with the FAISS index, and generating text responses.

### faiss_utils.py: 
Contains functions to initialize and interact with a FAISS index. FAISS (Facebook AI Similarity Search) is used to perform efficient similarity searches on vectorized text data (emergency descriptions). It includes:
initialize_faiss(): Initializes the FAISS index with embeddings of emergency keys.
find_closest_emergency(query): Finds the closest emergency in the database based on the user’s input.

### text_generation.py: 
Uses Hugging Face’s GPT-2 model to generate text responses. It includes:
get_llm_response(prompt): Generates text based on a given prompt using GPT-2.

### session_state.py: 
Manages user session states in Streamlit, specifically to track inactivity and provide warnings. It includes:
check_inactivity(): Checks the time since the last user interaction and displays a warning if the user is inactive for more than 30 seconds.
styles.py: Provides custom CSS styling for the Streamlit app to enhance the user interface, including setting a background image and styling layout components.

### constants.py: 
Contains a dictionary with predefined emergency responses that are used to provide immediate guidance in case of emergencies.








