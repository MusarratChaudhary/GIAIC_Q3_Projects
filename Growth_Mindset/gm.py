import streamlit as st
import random

# App Title
st.set_page_config(page_title="Growth Mindset Tips", page_icon="🌱")
st.title("🌱 Growth Mindset Daily Booster")
st.markdown("Welcome! 👋 Start your day with a powerful mindset tip.")

# List of growth mindset tips (you can add more!)
tips = [
    "🌟 Mistakes are proof you're trying.",
    "💡 Learn something new every day.",
    "🚀 Progress, not perfection.",
    "🧠 Challenges help you grow.",
    "🎁 Feedback is a gift — use it to improve!",
    "⏳ Growth takes time. Be patient with yourself.",
    "🔁 Fail, learn, repeat. That's growth!",
    "🔥 Don't stop until you're proud.",
    "👣 Small steps lead to big changes.",
    "🌈 Stay curious. Stay humble."
]

# Function to get a random tip
def get_random_tip():
    return random.choice(tips)

# Show tip
if st.button("✨ Show Me a Growth Tip"):
    tip = get_random_tip()
    st.success(tip)  # Green success box

# Optional static message
st.markdown("---")
st.markdown("💬 *Remember: Growth is a journey, not a race.*")

# Footer
st.caption("✨ Created with ❤️ by Musarrat Chaudhary using Python and Streamlit")
