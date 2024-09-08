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
1. Emergency Handling: Provides immediate guidance on emergencies based on predefined scenarios.
2. Message Handling: Allows users to leave messages that are forwarded to the doctor.
3. Natural Language Processing: Uses LLMs (GPT-2) to generate responses.
4. Vector Database Integration: Utilizes FAISS for efficient similarity search to match emergencies.
5. Asynchronous Processing: Implements delayed responses to simulate real-time data retrieval.

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
1. initialize_faiss(): Initializes the FAISS index with embeddings of emergency keys.
2. find_closest_emergency(query): Finds the closest emergency in the database based on the user’s input.

### text_generation.py: 
Uses Hugging Face’s GPT-2 model to generate text responses. It includes:
1. get_llm_response_async(prompt): Generates text based on a given prompt using GPT-2 asynchronously.

### session_state.py: 
Manages user session states in Streamlit, specifically to track inactivity and provide warnings. It includes:
1. check_inactivity(): Checks the time since the last user interaction and displays a warning if the user is inactive for more than 30 seconds.
   
### styles.py: 
Provides custom CSS styling for the Streamlit app to enhance the user interface, including setting a background image and styling layout components.

### constants.py: 
Contains a dictionary with predefined emergency responses that are used to provide immediate guidance in case of emergencies.

## How It Works
### Initialization: 
The app starts by initializing the FAISS index using predefined emergency scenarios. The background is set, and session states for inactivity tracking are initialized.

### User Interaction:
The user is prompted to indicate whether they are experiencing an emergency or want to leave a message.
Depending on the user's input:
1. Emergency: The user describes their emergency. The system searches for the closest match in the FAISS index. While simulating a delay (15 seconds) in fetching the emergency response, it asks for the user’s location.
2. Message: If the user wants to leave a message, the app collects the message and forwards it to the doctor.
   
### Emergency Handling:
Once an emergency is detected, the system checks the vector database for the closest match to the user's description.
The appropriate guidance is displayed from the dictionary, and additional guidance is generated using GPT-2.

### Inactivity Tracking: 
If the user is inactive for more than 30 seconds, a warning is displayed, prompting them to continue interacting with the app.

## Key Features and Improvements

### Async Programming:
Introduced a delay to simulate real-time data retrieval from the vector database.
### LLM Integration: 
Uses GPT-2 to enhance responses with natural language guidance.
### User-Friendly Interface: 
Leveraging Streamlit for an interactive UI that guides users through different emergency scenarios.

Ensure all dependencies are listed in requirements.txt and installed before running the application.
Recording Video of Working is also attached here.

## Conclusion
This AI receptionist system provides a robust framework for handling emergency scenarios and routine messages, enhancing the doctor's ability to respond promptly and effectively. The use of AI and machine learning technologies enables more responsive and context-aware assistance, improving patient outcomes in critical situations.








