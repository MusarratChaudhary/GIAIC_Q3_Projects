import streamlit as st
from cryptography.fernet import Fernet

# App Title and config
st.set_page_config(page_title="🔐 Secure Data Encryption", page_icon="🔏")
st.title("🔐 Secure Data Encryption Tool")
st.markdown("Encrypt and decrypt your text safely with this simple app.")

# Generate or load encryption key (For demo, generate once per session)
if "key" not in st.session_state:
    st.session_state.key = Fernet.generate_key()
    st.session_state.cipher_suite = Fernet(st.session_state.key)

# Show key (Optional, you can hide or remove this for real use)
st.write("**Encryption Key (Keep this secret!)**")
st.code(st.session_state.key.decode())

# Input text to encrypt
text_to_encrypt = st.text_area("Enter text to encrypt:")

if st.button("Encrypt"):
    if text_to_encrypt:
        encrypted_text = st.session_state.cipher_suite.encrypt(text_to_encrypt.encode())
        st.success("✅ Text encrypted successfully!")
        st.code(encrypted_text.decode())
        st.session_state.encrypted = encrypted_text.decode()
    else:
        st.warning("⚠️ Please enter some text to encrypt.")

# Input text to decrypt
st.markdown("---")
st.subheader("Decrypt your text")
encrypted_input = st.text_area("Enter encrypted text to decrypt:", value=st.session_state.get("encrypted", ""))

if st.button("Decrypt"):
    if encrypted_input:
        try:
            decrypted_text = st.session_state.cipher_suite.decrypt(encrypted_input.encode())
            st.success("✅ Text decrypted successfully!")
            st.code(decrypted_text.decode())
        except Exception as e:
            st.error("❌ Invalid encrypted text or wrong key!")
    else:
        st.warning("⚠️ Please enter encrypted text to decrypt.")

# Footer
st.markdown("---")
st.caption("✨ Created with ❤️ by Musarrat Chaudhary using Python and Streamlit")
