
from qachain import chain

import streamlit as st

def main():
    
    st.set_page_config(page_title="KG Chatbot", page_icon="💬")
    st.title("Knowledge Graph Chat Assistant")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Ask me anything about your knowledge graph!"}]
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    if prompt := st.chat_input("Type your question here..."):
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = chain.invoke(prompt).get('result')
                    st.write_stream((token + " " for token in response.split()))  # Streaming simulation
                except Exception as e:
                    response = f"Error: {str(e)}"
                    st.error(response)
            
            # Add assistant response to history
            st.session_state.messages.append({"role": "assistant", "content": response})
        

if __name__ =="__main__":
    main()