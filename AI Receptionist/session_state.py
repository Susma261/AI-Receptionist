#session_state.py
import streamlit as st
import time

def check_inactivity():
    current_time = time.time()
    if current_time - st.session_state.last_interaction_time > 30:  
        if not st.session_state.inactivity_warning_shown:
            st.warning("You have been inactive for a while. Please provide your input.")
            st.session_state.inactivity_warning_shown = True
    else:
        st.session_state.inactivity_warning_shown = False
