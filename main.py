import streamlit as st
from streamlit_chat import message

def main():
    st.set_page_config(
        page_title="Your own ChatGPT",
        page_icon="🤖"
    )

    st.header("Your own ChatGPT 🤖")

    # Display static chat messages
    message("Hello, how are you?", is_user=True)
    message("Hello, how are you?", is_user=False)

    # Sidebar user input
    with st.sidebar:
        user_input = st.text_input("Your message: ", key="user_input")

if __name__ == "__main__":
    main()
