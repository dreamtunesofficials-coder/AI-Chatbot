import streamlit as st
from google import genai
st.title("Introduction to Gemini Api")
 

    
user_input = st.text_input("Ask something to AI: ")
st.text(f"You : {user_input}")
    
    
API_KEY="AIzaSyD9hVS9Tqc-zUHqszQJFhZYVk8h23oEx_Q"

if 'response' not in st.session_state:
    st.session_state.response = ""
if st.button("Submit"):
    if user_input.strip():
        try:
            client= genai.Client(api_key=API_KEY)
            response=client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=user_input
        )
            st.session_state.response=response.text
        except Exception as e:
           st.error(f"An error occured : {str(e)}")
    else:
        st.warning("Please enter a question")
 
if st.session_state.response:
    st.text(f"Answer by Gemini: {st.session_state.response}")
    
            
        
        