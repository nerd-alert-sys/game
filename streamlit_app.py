import streamlit as st
import random

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Truth or Dare 🎭",
    page_icon="🎭",
    layout="centered"
)

# -----------------------------
# Data
# -----------------------------
TRUTHS = [
    "What is your biggest fear?",
    "Have you ever lied to your best friend?",
    "What is the most embarrassing thing that has happened to you?",
    "Who was your first crush?",
    "What secret have you never told anyone?",
    "What is the worst habit you have?",
    "Have you ever cheated on a test?",
    "What is something you regret?",
    "Who do you text the most?",
    "What is your biggest insecurity?"
]

DARES = [
    "Do 10 push-ups.",
    "Sing a song out loud.",
    "Do your best dance move for 15 seconds.",
    "Send a funny emoji to someone in your contacts.",
    "Speak in a funny accent for the next 2 minutes.",
    "Take a selfie with a silly face.",
    "Do 20 jumping jacks.",
    "Pretend to be an animal for 30 seconds.",
    "Say the alphabet backwards.",
    "Clap your hands above your head for 30 seconds."
]

# -----------------------------
# Session State Initialization
# -----------------------------
if "current_prompt" not in st.session_state:
    st.session_state.current_prompt = ""

if "current_type" not in st.session_state:
    st.session_state.current_type = ""

# -----------------------------
# UI
# -----------------------------
st.title("🎭 Truth or Dare Game")
st.markdown("Choose **Truth** or **Dare** and let the fun begin! 😄")

st.divider()

# Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("😇 Truth", use_container_width=True):
        st.session_state.current_type = "Truth"
        st.session_state.current_prompt = random.choice(TRUTHS)

with col2:
    if st.button("🔥 Dare", use_container_width=True):
        st.session_state.current_type = "Dare"
        st.session_state.current_prompt = random.choice(DARES)

st.divider()

# Display Result
if st.session_state.current_prompt:
    if st.session_state.current_type == "Truth":
        st.subheader("😇 Truth Question")
        st.info(st.session_state.current_prompt)
    else:
        st.subheader("🔥 Dare Challenge")
        st.warning(st.session_state.current_prompt)

# Reset Button
st.divider()
if st.button("🔄 Reset"):
    st.session_state.current_prompt = ""
    st.session_state.current_type = ""

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
