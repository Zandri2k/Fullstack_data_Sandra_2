import streamlit as st
from components.bot import Bot, GbGlenn_bot_action, JokeTeller_bot_action

def initialize_session_state():
    """Initialize session state variables """
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "bot" not in st.session_state:
        st.session_state.bot = Bot("""You always tell a funny joke, most of the times they're really bad but you finds it funny""")

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

        bot_response = st.session_state.bot.chat(prompt)
        response = f"Bot: {bot_response}"

        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

def layout():
    """Define the layout of the Streamlit app"""  
    chosen_bot = st.selectbox("choose one chatbot", options= ["GbGlenn", "JokeTeller"])

    st.title(f"{chosen_bot} was choosen")

    #st.write(f"{chosen_bot} is an extra ordinary chat bot with snapy respones and always close to funny joke.")
    display_chat_message()
    handler_user_input()

    bot_personalities = {"GbGlenn": GbGlenn_bot_action, "JokeTeller": JokeTeller_bot_action }
    st.session_state.bot = Bot(bot_personalities[chosen_bot])

    bot_introductions = {"GbGlenn": "is an extra ordinary chat bot with snapy respones and always close to funny joke.", "JokeTeller": "JokeTeller will always crack a funny joke"}
    st.write(f"{bot_introductions[chosen_bot]}")

if __name__ == "__main__":
    initialize_session_state() #This is the memory, state av sessionen.
    layout()

