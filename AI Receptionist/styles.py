#styles.py
import streamlit as st

def set_background():
    st.markdown("""
    <style>
    .left-col {
        background-image: url('https://designerapp.officeapps.live.com/designerapp/document.ashx?path=/ab438652-86ae-47f6-a2f8-18584745ee15/DallEGeneratedImages/dalle-bfbb94ff-0fd9-4ecc-89aa-db479bae2adc0251677035430408217400.jpg&dcHint=IndiaCentral&fileToken=4ed44a98-6eab-4249-93fa-ce88762cfe01');
        background-size: cover;
        height: 100vh;
        width:100%;
        background-position:center;
        
    }
    .right-col {
        height: 100vh;
        padding: 100px;
        width:100%;
    }
    </style>
    """, unsafe_allow_html=True)
