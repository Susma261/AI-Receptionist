import streamlit as st
import streamlit.components.v1 as components

# Create the JavaScript component
def inactivity_tracker():
    # JavaScript code to track user activity
    js_code = """
    <script>
    let timeout;
    function resetTimer() {
        clearTimeout(timeout);
        timeout = setTimeout(() => {
            // Send inactivity event to Streamlit
            const event = new CustomEvent('inactivity', { detail: { inactive: true } });
            window.dispatchEvent(event);
        }, 30000); // 30 seconds of inactivity
    }
    window.onload = function() {
        document.onmousemove = resetTimer;
        document.onkeypress = resetTimer;
        resetTimer(); // Initialize timer
    };

    // Listen for inactivity event
    window.addEventListener('inactivity', function(event) {
        const inactive = event.detail.inactive;
        if (typeof Streamlit !== 'undefined') {
            Streamlit.setComponentValue('inactive', inactive);
        }
    });
    </script>
    """
    components.html(js_code, height=0)

# Use the component in your Streamlit app
inactivity_tracker()
