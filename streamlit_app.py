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

WIN_POINTS = 10

# -----------------------------
# Game Data
# -----------------------------
TRUTHS = [
    {"text": "What is your biggest fear?", "difficulty": "Easy", "points": 2},
    {"text": "Have you ever lied to your best friend?", "difficulty": "Easy", "points": 2},
    {"text": "What is your most embarrassing moment?", "difficulty": "Medium", "points": 4},
    {"text": "What secret have you never told anyone?", "difficulty": "Hard", "points": 6},
]

DARES = [
    {"text": "Do 10 push-ups.", "difficulty": "Easy", "points": 2},
    {"text": "Sing a song out loud.", "difficulty": "Easy", "points": 2},
    {"text": "Dance for 30 seconds.", "difficulty": "Medium", "points": 4},
    {"text": "Speak in an accent for 2 minutes.", "difficulty": "Medium", "points": 4},
    {"text": "Do 30 jumping jacks.", "difficulty": "Hard", "points": 6},
]

# -----------------------------
# Session State Initialization
# -----------------------------
defaults = {
    "p1_score": 0,
    "p2_score": 0,
    "p1_card": None,
    "p2_card": None,
    "rounds_played": 0,
    "game_over": False,
    "winner": None,
}

for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# -----------------------------
# Difficulty Scaling Logic
# -----------------------------
def weighted_cards(cards, rounds):
    """
    As rounds increase, Hard cards become more likely
    """
    weighted = []
    for card in cards:
        if card["difficulty"] == "Easy":
            weight = max(1, 5 - rounds)
        elif card["difficulty"] == "Medium":
            weight = 3 + rounds
        else:  # Hard
            weight = 1 + rounds * 2

        weighted.extend([card] * weight)

    return random.choice(weighted)

def draw_card(card_type):
    st.session_state.rounds_played += 1
    if card_type == "Truth":
        return weighted_cards(TRUTHS, st.session_state.rounds_played)
    else:
        return weighted_cards(DARES, st.session_state.rounds_played)

# -----------------------------
# Win Check
# -----------------------------
def check_winner():
    if st.session_state.p1_score >= WIN_POINTS:
        st.session_state.game_over = True
        st.session_state.winner = "Player 1"
    elif st.session_state.p2_score >= WIN_POINTS:
        st.session_state.game_over = True
        st.session_state.winner = "Player 2"

# -----------------------------
# UI
# -----------------------------
st.title("🎭 Truth or Dare — 2 Player Challenge")
st.caption(f"First to **{WIN_POINTS} points** wins 🏆")

st.divider()

# -----------------------------
# Winner Announcement
# -----------------------------
if st.session_state.game_over:
    loser = "Player 2" if st.session_state.winner == "Player 1" else "Player 1"
    st.success(f"🏆 **{st.session_state.winner} wins!**")
    st.error(f"🍻 **{loser}, take a drink!**")

# -----------------------------
# Player Panels
# -----------------------------
col1, col2 = st.columns(2)

# ===== PLAYER 1 =====
with col1:
    st.subheader("👤 Player 1")
    st.metric("Score", st.session_state.p1_score)

    if not st.session_state.game_over:
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
        st.caption(f"Difficulty: {card['difficulty']} | Points: {card['points']}")

        if st.button("✅ Completed (P1)"):
            st.session_state.p1_score += card["points"]
            st.session_state.p1_card = None
            check_winner()

# ===== PLAYER 2 =====
with col2:
    st.subheader("👤 Player 2")
    st.metric("Score", st.session_state.p2_score)

    if not st.session_state.game_over:
        c1, c2 = st.columns(2)
        with c1:
            if st.button("😇 Truth (P2)", use_container_width=True):
                st.session_state.p2_card = draw_card("Truth")

        with c2:
            if st.button("🔥 Dare (P2)", use_container_width=True):
                st.session_state.p2_card = draw_card("Dare")

    if st.session_state.p2_card:
        card = st.session_state.p2_card
        st.warning(f"**{card['text']}**")
        st.caption(f"Difficulty: {card['difficulty']} | Points: {card['points']}")

        if st.button("✅ Completed (P2)"):
            st.session_state.p2_score += card["points"]
            st.session_state.p2_card = None
            check_winner()

# -----------------------------
# Reset Controls
# -----------------------------
st.divider()
col_r1, col_r2 = st.columns(2)

with col_r1:
    if st.button("🔄 Reset Game"):
        st.session_state.p1_score = 0
        st.session_state.p2_score = 0
        st.session_state.p1_card = None
        st.session_state.p2_card = None
        st.session_state.game_over = False
        st.session_state.winner = None

with col_r2:
    if st.button("🧹 Master Reset"):
        for k, v in defaults.items():
            st.session_state[k] = v

st.caption("Built with ❤️ using Streamlit")
