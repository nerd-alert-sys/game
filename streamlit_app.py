import streamlit as st
import random

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Truth or Dare: NAN vs ACE",
    page_icon="🔥",
    layout="wide"
)

# Constants
WIN_POINTS = 20 # Increased points needed to win since we have more content
PLAYERS = {1: "NAN", 2: "ACE"}

# -----------------------------
# Game Data (40+ items each)
# -----------------------------
TRUTHS = [
    # --- EASY (1-3 Points) ---
    {"text": "What is your favorite meal?", "difficulty": "Easy", "points": 1},
    {"text": "What is the last movie that made you cry?", "difficulty": "Easy", "points": 2},
    {"text": "Who is your celebrity crush?", "difficulty": "Easy", "points": 2},
    {"text": "Do you sing in the shower?", "difficulty": "Easy", "points": 1},
    {"text": "What is your biggest pet peeve?", "difficulty": "Easy", "points": 2},
    {"text": "Have you ever cheated on a test?", "difficulty": "Easy", "points": 2},
    {"text": "When was the last time you brushed your teeth?", "difficulty": "Easy", "points": 1},
    {"text": "What is a talent you wish you had?", "difficulty": "Easy", "points": 2},
    {"text": "What is the worst gift you've ever received?", "difficulty": "Easy", "points": 2},
    {"text": "Have you ever stalked an ex on social media?", "difficulty": "Easy", "points": 2},
    {"text": "What is your guilty pleasure song?", "difficulty": "Easy", "points": 2},
    {"text": "Boxers or briefs (or granny panties)?", "difficulty": "Easy", "points": 1},
    {"text": "Have you ever ghosted someone?", "difficulty": "Easy", "points": 2},
    
    # --- MEDIUM (4-6 Points) ---
    {"text": "What is the most embarrassing thing you've done in public?", "difficulty": "Medium", "points": 4},
    {"text": "Have you ever practiced kissing on your hand?", "difficulty": "Medium", "points": 4},
    {"text": "What is the biggest lie you've ever told your parents?", "difficulty": "Medium", "points": 5},
    {"text": "Who in this room would you save first in a zombie apocalypse?", "difficulty": "Medium", "points": 5},
    {"text": "What is the meanest thing you've ever said to someone?", "difficulty": "Medium", "points": 5},
    {"text": "Have you ever picked your nose and ate it?", "difficulty": "Medium", "points": 6},
    {"text": "What is a secret you’ve kept from your best friend?", "difficulty": "Medium", "points": 6},
    {"text": "Have you ever peed in a pool?", "difficulty": "Medium", "points": 4},
    {"text": "What is the most trouble you've ever been in?", "difficulty": "Medium", "points": 5},
    {"text": "Have you ever sent a sext to the wrong person?", "difficulty": "Medium", "points": 6},
    {"text": "When was the last time you wet the bed?", "difficulty": "Medium", "points": 6},
    {"text": "What is the cringiest thing you posted on social media?", "difficulty": "Medium", "points": 4},
    
    # --- HARD / SPICY (7-10 Points) ---
    {"text": "What is your wildest fantasy?", "difficulty": "Hard", "points": 8},
    {"text": "Have you ever had a crush on a friend's partner?", "difficulty": "Hard", "points": 9},
    {"text": "What is the weirdest place you have ever done 'it'?", "difficulty": "Hard", "points": 10},
    {"text": "Rate the other player's looks on a scale of 1 to 10.", "difficulty": "Hard", "points": 8},
    {"text": "What is the most illegal thing you have ever done?", "difficulty": "Hard", "points": 9},
    {"text": "Who was your worst kiss and why?", "difficulty": "Hard", "points": 8},
    {"text": "Have you ever gone skinny dipping?", "difficulty": "Hard", "points": 7},
    {"text": "What is your favorite body part on the other player?", "difficulty": "Hard", "points": 9},
    {"text": "Have you ever flashed someone?", "difficulty": "Hard", "points": 9},
    {"text": "What is something you’ve done in bed that you’d never tell your parents?", "difficulty": "Hard", "points": 10},
    {"text": "If you had to sleep with one person from your work/school, who would it be?", "difficulty": "Hard", "points": 9},
    {"text": "What color is your underwear right now? Show proof.", "difficulty": "Hard", "points": 8},
    {"text": "Have you ever sent a nude photo?", "difficulty": "Hard", "points": 8},
]

DARES = [
    # --- EASY (1-3 Points) ---
    {"text": "Do 10 push-ups.", "difficulty": "Easy", "points": 2},
    {"text": "Sing the chorus of a pop song loudly.", "difficulty": "Easy", "points": 2},
    {"text": "Talk in a British accent until your next turn.", "difficulty": "Easy", "points": 3},
    {"text": "Do your best chicken impression.", "difficulty": "Easy", "points": 2},
    {"text": "Let the other player tickle you for 10 seconds.", "difficulty": "Easy", "points": 3},
    {"text": "Hold your breath for 20 seconds.", "difficulty": "Easy", "points": 1},
    {"text": "Spin around 10 times and try to walk straight.", "difficulty": "Easy", "points": 2},
    {"text": "Send a 'I love you' text to your mom.", "difficulty": "Easy", "points": 3},
    {"text": "Do 20 squats.", "difficulty": "Easy", "points": 2},
    {"text": "Let the other player style your hair.", "difficulty": "Easy", "points": 3},
    {"text": "Show the last photo in your camera roll.", "difficulty": "Easy", "points": 2},
    {"text": "Plank for 30 seconds.", "difficulty": "Easy", "points": 3},
    {"text": "Bark like a dog every time you speak for the next minute.", "difficulty": "Easy", "points": 2},

    # --- MEDIUM (4-6 Points) ---
    {"text": "Let the other player go through your phone for 30 seconds.", "difficulty": "Medium", "points": 6},
    {"text": "Eat a spoonful of hot sauce or mustard.", "difficulty": "Medium", "points": 5},
    {"text": "Dance without music for 1 minute.", "difficulty": "Medium", "points": 4},
    {"text": "Call a random contact and sing Happy Birthday.", "difficulty": "Medium", "points": 6},
    {"text": "Let the other player draw on your face with a pen.", "difficulty": "Medium", "points": 6},
    {"text": "Put an ice cube down your shirt/pants.", "difficulty": "Medium", "points": 5},
    {"text": "Lick the floor (or a wall).", "difficulty": "Medium", "points": 6},
    {"text": "Post an embarrassing status on Facebook/Twitter.", "difficulty": "Medium", "points": 6},
    {"text": "Smell the other player's socks.", "difficulty": "Medium", "points": 4},
    {"text": "Do a cartwheel (or attempt one).", "difficulty": "Medium", "points": 4},
    {"text": "Let the other player give you a wedgie.", "difficulty": "Medium", "points": 5},
    {"text": "Walk like a crab to the other side of the room.", "difficulty": "Medium", "points": 4},

    # --- HARD / NAUGHTY (7-10 Points) ---
    {"text": "Give the other player a sensual massage for 2 minutes.", "difficulty": "Hard", "points": 9},
    {"text": "Twerk for 30 seconds.", "difficulty": "Hard", "points": 8},
    {"text": "Let the other player kiss you anywhere they want (face/neck).", "difficulty": "Hard", "points": 10},
    {"text": "Take off one article of clothing (accessories don't count).", "difficulty": "Hard", "points": 9},
    {"text": "Whisper something dirty in the other player's ear.", "difficulty": "Hard", "points": 8},
    {"text": "Kiss the other player on the neck.", "difficulty": "Hard", "points": 9},
    {"text": "Let the other player spank you.", "difficulty": "Hard", "points": 10},
    {"text": "Sit on the other player's lap for the next 2 rounds.", "difficulty": "Hard", "points": 9},
    {"text": "Moan loudly as if you are enjoying yourself.", "difficulty": "Hard", "points": 8},
    {"text": "Send a risky text to your crush/partner dictated by the other player.", "difficulty": "Hard", "points": 10},
    {"text": "Blindfold yourself and let the other player feed you something.", "difficulty": "Hard", "points": 8},
    {"text": "Give a lap dance to the other player.", "difficulty": "Hard", "points": 10},
    {"text": "Perform a striptease (keep underwear on) for 1 minute.", "difficulty": "Hard", "points": 10},
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
# Difficulty Scaling Logic
# -----------------------------
def weighted_cards(cards, rounds):
    weighted = []
    for card in cards:
        if card["difficulty"] == "Easy":
            # Easy cards become less likely as rounds go up
            weight = max(1, 6 - int(rounds/2))
        elif card["difficulty"] == "Medium":
            # Medium cards peak in the middle
            weight = 3 + int(rounds/2)
        else:  # Hard
            # Hard cards become much more likely later
            weight = 1 + int(rounds)
        weighted.extend([card] * weight)
    return random.choice(weighted)

def draw_card(card_type):
    st.session_state.rounds_played += 1
    st.session_state.current_type = card_type
    return weighted_cards(
        TRUTHS if card_type == "Truth" else DARES,
        st.session_state.rounds_played
    )

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
        st.session_state.winner = PLAYERS[1]
    elif st.session_state.p2_score >= WIN_POINTS:
        st.session_state.game_over = True
        st.session_state.winner = PLAYERS[2]

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.header("📊 Scoreboard")
    st.metric(f"🦄 {PLAYERS[1]}", st.session_state.p1_score)
    st.metric(f"🦅 {PLAYERS[2]}", st.session_state.p2_score)
    
    st.progress(min(1.0, (st.session_state.p1_score + st.session_state.p2_score) / (WIN_POINTS * 2)))
    st.caption(f"Goal: {WIN_POINTS} points")

    st.divider()
    st.subheader("🎯 Current Turn")
    st.info(f"**{PLAYERS[st.session_state.current_player]}** is playing")

    st.divider()
    if st.button("🔄 Reset Game", use_container_width=True):
        st.session_state.p1_score = 0
        st.session_state.p2_score = 0
        st.session_state.current_player = 1
        st.session_state.current_card = None
        st.session_state.current_type = None
        st.session_state.rounds_played = 0
        st.session_state.game_over = False
        st.session_state.winner = None
        st.rerun()

# -----------------------------
# Main Panel
# -----------------------------
st.title("🔥 Truth or Dare: NAN vs ACE")
st.caption(f"Spicy Edition • First to {WIN_POINTS} points wins 🏆")

st.divider()

# Winner Display
if st.session_state.game_over:
    winner_name = st.session_state.winner
    loser_name = PLAYERS[1] if winner_name == PLAYERS[2] else PLAYERS[2]
    
    st.success(f"🏆 **{winner_name} WINS THE GAME!**")
    st.error(f"💀 **{loser_name}, you must take a penalty shot or do a Double Dare!**")
    st.balloons()

# Gameplay
if not st.session_state.game_over:
    current_name = PLAYERS[st.session_state.current_player]
    st.subheader(f"🎲 {current_name}'s Turn")

    # Only show draw buttons if no card is currently active
    if st.session_state.current_card is None:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("😇 TRUTH", use_container_width=True, type="primary"):
                st.session_state.current_card = draw_card("Truth")
                st.rerun()

        with col2:
            if st.button("😈 DARE", use_container_width=True, type="secondary"):
                st.session_state.current_card = draw_card("Dare")
                st.rerun()

# Card Display
if st.session_state.current_card:
    card = st.session_state.current_card
    
    # Visual flair based on difficulty
    if card['difficulty'] == 'Easy':
        border_color = "green"
        emoji = "🌱"
    elif card['difficulty'] == 'Medium':
        border_color = "orange"
        emoji = "🌶️"
    else:
        border_color = "red"
        emoji = "🔥"

    st.markdown(f"""
    <div style="padding: 20px; border: 2px solid {border_color}; border-radius: 10px; margin: 20px 0; background-color: #262730;">
        <h3 style="text-align: center; color: white;">{emoji} {card['difficulty'].upper()} {emoji}</h3>
        <h2 style="text-align: center; color: white;">{card['text']}</h2>
        <p style="text-align: center; color: #aaa;">Points: {card['points']}</p>
    </div>
    """, unsafe_allow_html=True)

    col_success, col_fail = st.columns(2)

    # COMPLETED
    with col_success:
        if st.button("✅ Completed", use_container_width=True):
            add_points(card["points"])
            st.toast(f"🎉 +{card['points']} Points for {PLAYERS[st.session_state.current_player]}!", icon="🎉")
            st.session_state.current_card = None
            check_winner()
            if not st.session_state.game_over:
                switch_player()
            st.rerun()

    # FAILED
    with col_fail:
        if st.button("❌ Failed / Refused", use_container_width=True):
            st.error(f"👎 Weak! No points for {PLAYERS[st.session_state.current_player]}!")
            st.session_state.current_card = None
            switch_player()
            st.rerun()

st.divider()
st.caption("Game logic scales difficulty: The longer you play, the spicier it gets.")
