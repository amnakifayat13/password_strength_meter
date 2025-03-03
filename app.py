import streamlit as st
import re
import math
import random

def check_password_strength(password):
    score = 0
    messages = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        messages.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]" , password) and re.search(r"[a-z]", password):
        score += 1
    else:
        messages.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        messages.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        messages.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    st.markdown("---")
    if score == 4:
        st.markdown("<p style='color:green; font-size:20px;'>✅ Strong Password!</p>", unsafe_allow_html=True)
    elif score == 3:
        st.markdown("<p style='color:orange; font-size:18px;'>⚠️ Moderate Password - Consider adding more security features.</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color:red; font-size:18px;'>❌ Weak Password - Improve it using the suggestions below:</p>", unsafe_allow_html=True)
    
    for msg in messages:
        st.markdown(f"<p style='color:red;'>{msg}</p>", unsafe_allow_html=True)

# Generate Random Password
option = ["Pq7$kL@3","X9yT$2Lm","A1@kFp%3","Z2fL@p7T","mL9$Xq1K"]
choose = math.floor(random.random()*len(option))
random_password = option[choose]

# Custom CSS for styling
st.markdown("""
    <style>
        .stTextInput>div>div>input {
            border: 2px solid #4CAF50;
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 10px;
            border: none;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# Title & Input Field
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🔐 Password Strength Meter</h1>", unsafe_allow_html=True)
password = st.text_input("Enter your password:", type="password")

# Button to check password strength
if st.button("Check Password Strength"):
    if password:
        check_password_strength(password)
    else:
        st.markdown(f"<p style='color:blue; font-size:16px;'>💡 Enter a Password? Suggest this one: <b>{random_password}</b></p>", unsafe_allow_html=True)
