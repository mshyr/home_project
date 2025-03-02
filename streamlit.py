import streamlit as st

st.markdown("""
    <style>
    div.stButton > button {
        background-color: Orange; /* Background color */
        color: White; /* Text color */
        font-size: 40px; /* Font size */
        border-radius: 10px; /* Rounded corners */
        padding: 10px 20px; /* Padding */
        border: 2px solid black; /* Border */      
        
    }
 
   
    </style>
""", unsafe_allow_html=True)


name = st.text_input("Name")
age = st.number_input("Age",value=None, placeholder="age")

if st.button("Submit"):
    st.title("Welcome")
    st.write(f"My name is {name}")
    st.write(f"i am {age} Years Old")
