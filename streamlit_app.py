import streamlit as st
import random

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Truth or Dare - 2 Player",
    page_icon="🎭",
    layout="wide"
)

# -----------------------------
# Game Data (Question, Difficulty, Points)
# -----------------------------
TRUTHS = [
    {"text": "What is your biggest fear?", "difficulty": "Easy", "points": 5},
    {"text": "Have you ever lied to your best friend?", "difficulty": "Easy", "points": 5},
    {"text": "What is your most embarrassing moment?", "difficulty": "Medium", "points": 10},
    {"text": "What secret have you never told anyone?", "difficulty": "Hard", "points": 20},
    {"text": "What is your biggest regret?", "difficulty": "Hard", "points": 20},
]

DARES = [
    {"text": "Do 10 push-ups.", "difficulty": "Easy", "points": 5},
    {"text": "Sing a song out loud.", "difficulty": "Easy", "points": 5},
    {"text": "Dance for 30 seconds.", "difficulty": "Medium", "points": 10},
    {"text": "Speak in an accent for 2 minutes.", "difficulty": "Medium", "points": 10},
    {"text": "Do 30 jumping jacks.", "difficulty": "Hard", "points": 20},
]

# -----------------------------
# Session State Initialization
# -----------------------------
for key in [
    "p1_score", "p2_score",
    "p1_card", "p2_card"
]:
    if key not in st.session_state:
        st.session_state[key] = 0 if "score" in key else None

# -----------------------------
# Helper Function
# -----------------------------
def draw_card(card_type):
    if card_type == "Truth":
        return random.choice(TRUTHS)
    else:
        return random.choice(DARES)

# -----------------------------
# UI
# -----------------------------
st.title("🎭 Truth or Dare — 2 Player Game with Points")
st.markdown("Complete the challenge to **earn points** ⭐")

st.divider()

# -----------------------------
# Player Panels
# -----------------------------
col1, col2 = st.columns(2)

# ===== PLAYER 1 =====
with col1:
    st.subheader("👤 Player 1")
    st.metric("Score", st.session_state.p1_score)

    c1, c2 = st.columns(2)
    with c1:
        if st.button("😇 Truth (P1)", use_container_width=True):
            st.session_state.p1_card = draw_card("Truth")

    with c2:
        if st.button("🔥 Dare (P1)", use_container_width=True):
            st.session_state.p1_card = draw_card("Dare")

    if st.session_state.p1_card:
        card = st.session_state.p1_card
        st.info(f"**{card['text']}**")
        st.caption(f"Difficulty: {card['difficulty']
