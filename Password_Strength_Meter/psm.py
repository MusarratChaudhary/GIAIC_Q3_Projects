import streamlit as st

# Set page configuration
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐", layout="centered")

# Custom header
st.markdown("<h1 style='text-align: center; color: teal;'>🔒 Check Your Password Strength</h1>", unsafe_allow_html=True)
st.write("👋 Welcome! This simple app tells you if your password is **Strong**, **Medium**, or **Weak** based on common security rules.")

# Function to check password strength
def check_strength(password):
    strength = 0

    # Rule 1: Minimum length should be 8 characters
    if len(password) >= 8:
        strength += 1

    # Rule 2: At least one number
    if any(char.isdigit() for char in password):
        strength += 1

    # Rule 3: At least one uppercase letter
    if any(char.isupper() for char in password):
        strength += 1

    # Rule 4: At least one special character
    if any(char in "!@#$%^&*()-_=+[]{};:,.<>?/|" for char in password):
        strength += 1

    # Decision based on strength score
    if strength <= 1:
        return "🔴 Weak"
    elif strength == 2 or strength == 3:
        return "🟠 Medium"
    else:
        return "🟢 Strong"

# Input box with password masking
password = st.text_input("🔑 Enter your password below:", type="password")

# Check and display strength only if password is entered
if password:
    result = check_strength(password)
    
    st.markdown(f"<h3 style='color: purple;'>Your Password Strength is: {result}</h3>", unsafe_allow_html=True)

    # Tips
    st.info("💡 Tip: Use a mix of capital letters, numbers, and symbols for a strong password.")

# Footer
st.markdown("---")
st.caption("✨ Created with ❤️ by Musarrat Chaudhary using Python and Streamlit")


