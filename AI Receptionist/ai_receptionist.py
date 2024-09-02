#ai_receptionist.py
import streamlit as st
import numpy as np
import time
from faiss_utils import initialize_faiss, find_closest_emergency
from text_generation import get_llm_response
from session_state import check_inactivity
from styles import set_background
from constants import emergency_responses 


initialize_faiss()

st.title("Dr. Ardin's AI Receptionist")

set_background()

col1, col2 = st.columns([1, 1])  

with col1:
    st.markdown('<div class="left-col"></div>', unsafe_allow_html=True)

with col2:
    if 'last_interaction_time' not in st.session_state:
        st.session_state.last_interaction_time = time.time()
    if 'inactivity_warning_shown' not in st.session_state:
        st.session_state.inactivity_warning_shown = False

    check_inactivity()  

    user_input = st.text_input("Are you experiencing an emergency or would you like to leave a message?")
    if user_input:
        st.session_state.last_interaction_time = time.time()  
        check_inactivity()  

        if "emergency" in user_input.lower():
            st.write("What is your emergency?")
            emergency_input = st.text_input("Describe your emergency:")
            
            if emergency_input:
                st.session_state.last_interaction_time = time.time()  
                check_inactivity()  
                closest_emergency, distance = find_closest_emergency(emergency_input)
                
                with st.spinner("Checking the database for guidance..."):
                    time.sleep(15)  
                
                llm_prompt = f"Provide first aid guidance for the situation: {emergency_input}"
                additional_guidance = get_llm_response(llm_prompt)
                
                st.write(f"Guidance found for: {closest_emergency}")
                st.write(emergency_responses[closest_emergency])
                st.write(f"Additional guidance from GPT-2: {additional_guidance}")
                
                user_location = st.text_input("Meanwhile, can you tell me which area you are located in right now?")
                
                if user_location:
                    st.session_state.last_interaction_time = time.time()  
                    st.write(f"Dr. Ardin will be coming to your location in approximately {np.random.randint(5, 15)} minutes.")
                    st.write("Please follow the steps while you wait.")
                    
                    
                    action = st.radio("Is there anything else I can assist you with?", 
                                      ["Leave Message", "Provide feedback", "Schedule appointment", "End this session"])
                    
                    if action == "Leave Message":
                        new_question = st.text_input("Enter message:")
                        if new_question:
                            st.write("Thank you for the message. We will get back to you soon.")
                    
                    elif action == "Provide feedback":
                        feedback = st.text_area("Enter your feedback:")
                        if feedback:
                            st.write("Thank you for your feedback. We appreciate your input.")
                    
                    elif action == "Schedule appointment":
                        st.write("Please provide your preferred date and time for the new appointment:")
                        new_appointment_date = st.date_input("New Appointment Date")
                        new_appointment_time = st.time_input("New Appointment Time")
                        
                        if new_appointment_date and new_appointment_time:
                            st.write(f"Your new appointment is scheduled for {new_appointment_date} at {new_appointment_time}.")
                            st.session_state.last_interaction_time = time.time()  
                        
                    elif action == "End this session":
                        st.write("Thank you for using Dr. Ardin's AI Receptionist. If you need further assistance, feel free to come back.")
                        st.session_state.last_interaction_time = time.time()  
                    
        else:
            st.write("Please provide your message:")
            message = st.text_area("Enter your message:")
            
            if message:
                st.session_state.last_interaction_time = time.time()  
                check_inactivity()  
                st.write("Thanks for the message, we will forward it to Dr. Ardin.")
                
                schedule_appointment = st.radio("Would you like to schedule an appointment with Dr. Ardin?", ["Yes", "No"])
                
                if schedule_appointment == "Yes":
                    st.write("Please provide your preferred date and time for the appointment:")
                    appointment_date = st.date_input("Appointment Date")
                    appointment_time = st.time_input("Appointment Time")
                    
                    if appointment_date and appointment_time:
                        st.write(f"Your appointment is scheduled for {appointment_date} at {appointment_time}.")
                        st.session_state.last_interaction_time = time.time()  
                
                elif schedule_appointment == "No":
                    st.write("Thank you for your message. If you need further assistance, feel free to ask.")
