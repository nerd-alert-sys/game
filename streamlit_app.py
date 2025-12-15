import streamlit as st
import random

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Truth or Dare",
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
    "current_player": 1,
    "current_card": None,
    "current_type": None,
    "rounds_played": 0,
    "game_over": False,
    "winner": None,
}

for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# -----------------------------
# Difficulty Scaling
# -----------------------------
def weighted_cards(cards, rounds):
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
    st.session_state.current_type = card_type
    if card_type == "Truth":
        return weighted_cards(TRUTHS, st.session_state.rounds_played)
    else:
        return weighted_cards(DARES, st.session_state.rounds_played)

# -----------------------------
# Game Logic
# -----------------------------
def switch_player():
    st.session_state.current_player = 2 if st.session_state.current_player == 1 else 1

def add_points(points):
    if st.session_state.current_player == 1:
        st.session_state.p1_score += points
    else:
        st.session_state.p2_score += points

def check_winner():
    if st.session_state.p1_score >= WIN_POINTS:
        st.session_state.game_over = True
        st.session_state.winner = "Player 1"
    elif st.session_state.p2_score >= WIN_POINTS:
        st.session_state.game_over = True
        st.session_state.winner = "Player 2"

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.header("📊 Scoreboard")
    st.metric("👤 Player 1", st.session_state.p1_score)
    st.metric("👤 Player 2", st.session_state.p2_score)

    st.divider()
    st.subheader("🎯 Current Turn")
    st.write(f"**Player {st.session_state.current_player}**")

    st.divider()
    if st.button("🔄 Reset Game", use_container_width=True):
        st.session_state.p1_score = 0
        st.session_state.p2_score = 0
        st.session_state.current_player = 1
        st.session_state.current_card = None
        st.session_state.current_type = None
        st.session_state.game_over = False
        st.session_state.winner = None

    if st.button("🧹 Master Reset", use_container_width=True):
        for k, v in defaults.items():
            st.session_state[k] = v

# -----------------------------
# Main Panel
# -----------------------------
st.title("🎭 Truth or Dare")
st.caption("Players alternate turns — first to 10 points wins 🏆")

st.divider()

# Winner
if st.session_state.game_over:
    loser = "Player 2" if st.session_state.winner == "Player 1" else "Player 1"
    st.success(f"🏆 **{st.session_state.winner} wins!**")
    st.error(f"🍻 **{loser}, take a drink!**")

# Gameplay
if not st.session_state.game_over:
    st.subheader(f"👤 Player {st.session_state.current_player}'s Turn")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("😇 Truth", use_container_width=True):
            st.session_state.current_card = draw_card("Truth")

    with col2:
        if st.button("🔥 Dare", use_container_width=True):
            st.session_state.current_card = draw_card("Dare")

# Card Display
if st.session_state.current_card:
    card = st.session_state.current_card
    st.info(f"**{card['text']}**")
    st.caption(f"Difficulty: {card['difficulty']} | Points: {card['points']}")

    col_success, col_fail = st.columns(2)

    # COMPLETE
    with col_success:
        if st.button("✅ Completed", use_container_width=True):
            add_points(card["points"])
            st.balloons()
            st.toast("🎉 Challenge completed! Points awarded!", icon="🎉")
            st.session_state.current_card = None
            check_winner()
            if not st.session_state.game_over:
                switch_player()

    # FAIL (only for dares)
    if st.session_state.current_type == "Dare":
        with col_fail:
            if st.button("❌ Failed", use_container_width=True):
                st.error("👎 BOOO! Challenge failed!")
                st.toast("👎 No points for you!", icon="👎")
                st.session_state.current_card = None
                switch_player()

st.caption("Built with ❤️ using Streamlit")
