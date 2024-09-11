import streamlit as st
from components.bot import Bot

def initialize_session_state():
    """Initialize session state variables """
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "bot" not in st.session_state:
        st.session_state.bot = Bot()

def display_chat_message():
    """Display chat message from history"""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def handler_user_input():
    """Handle user input and generate bot response."""
    if prompt := st.chat_input("Wassup? I'm ready!"):
        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.messages.append({"role": "user", "content": prompt})

        bot_response = st.session_State.bot.chat(prompt)
        response = f"GbGlenn: {bot_response}"

        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

def layout():
    """Define the layout of the Streamlit app"""  
    st.title("Chat with GbGlenn")
    st.write("GbGlenn is an extra ordinary chat bot with snapy respones and always close to funny joke.")
    display_chat_message()
    handler_user_input()

if __name__ == "__main__":
    initialize_session_state() #This is the memory, state av sessionen.
    layout()