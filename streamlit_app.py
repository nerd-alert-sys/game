import streamlit as st
import random

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Truth or Dare",
    page_icon="🔥",
    layout="wide"
)

# Constants
WIN_POINTS = 20 

# -----------------------------
# Game Data
# -----------------------------
TRUTHS = [
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
    {"text": "Who is the messy one in your family?", "difficulty": "Easy", "points": 2},
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
    {"text": "Have you ever hooked up with a stranger?", "difficulty": "Hard", "points": 9},
]

DARES = [
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
    {"text": "Drink a glass of water without using your hands.", "difficulty": "Easy", "points": 3},
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
    {"text": "Let the other player put their hand down your pants for 30 seconds.", "difficulty": "Hard", "points": 10},
]

# -----------------------------
# Session State Initialization
# -----------------------------
if "setup_complete" not in st.session_state:
    st.session_state.setup_complete = False

# Only initialize these if they don't exist
defaults = {
    "p1_name": "Player 1",
    "p2_name": "Player 2",
    "p1_score": 0,
    "p2_score": 0,
    "current_player": 1,
    "current_card": None,
    "current_type": None,
    "rounds_played": 0,
    "game_over": False,
    "winner": None,
    "used_truths": set(),
    "used_dares": set(),
}

for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# -----------------------------
# UTILITY FUNCTIONS
# -----------------------------

def get_random_card(card_type, rounds):
    """Selects a random card based on difficulty weights and history."""
    if card_type == "Truth":
        source_list = TRUTHS
        used_set = st.session_state.used_truths
    else:
        source_list = DARES
        used_set = st.session_state.used_dares

    available_indices = [i for i in range(len(source_list)) if i not in used_set]

    if not available_indices:
        st.toast(f"🔄 All {card_type}s used! Reshuffling deck...", icon="🃏")
        used_set.clear()
        available_indices = list(range(len(source_list)))

    weighted_indices = []
    for i in available_indices:
        card = source_list[i]
        if card["difficulty"] == "Easy":
            weight = max(1, 6 - int(rounds/2))
        elif card["difficulty"] == "Medium":
            weight = 3 + int(rounds/2)
        else:
            weight = 1 + int(rounds)
        weighted_indices.extend([i] * weight)

    selected_index = random.choice(weighted_indices)
    used_set.add(selected_index)
    return source_list[selected_index]

# --- ACTION HANDLERS (CALLBACKS) ---
# These functions run BEFORE the page reloads, ensuring scores update instantly

def draw_new_card(card_type):
    st.session_state.rounds_played += 1
    st.session_state.current_type = card_type
    st.session_state.current_card = get_random_card(card_type, st.session_state.rounds_played)

def handle_completion(points):
    # 1. Add Points to CURRENT player
    if st.session_state.current_player == 1:
        st.session_state.p1_score += points
    else:
        st.session_state.p2_score += points
    
    # 2. Check Win Condition
    if st.session_state.p1_score >= WIN_POINTS:
        st.session_state.game_over = True
        st.session_state.winner = st.session_state.p1_name
    elif st.session_state.p2_score >= WIN_POINTS:
        st.session_state.game_over = True
        st.session_state.winner = st.session_state.p2_name
    
    # 3. Clear Card and Switch Player (if game not over)
    st.session_state.current_card = None
    if not st.session_state.game_over:
        st.session_state.current_player = 2 if st.session_state.current_player == 1 else 1

def handle_failure():
    # Just switch player, no points
    st.session_state.current_card = None
    st.session_state.current_player = 2 if st.session_state.current_player == 1 else 1

# -----------------------------
# SETUP SCREEN
# -----------------------------
if not st.session_state.setup_complete:
    st.title("🔥 Truth or Dare: Setup")
    col1, col2 = st.columns(2)
    with col1:
        p1_input = st.text_input("Player 1 Name", value="Player 1")
    with col2:
        p2_input = st.text_input("Player 2 Name", value="Player 2")
        
    if st.button("Start Game", type="primary"):
        st.session_state.p1_name = p1_input
        st.session_state.p2_name = p2_input
        st.session_state.setup_complete = True
        st.rerun()
    st.stop()

# Helper Dictionary for Names
PLAYERS = {1: st.session_state.p1_name, 2: st.session_state.p2_name}

# -----------------------------
# SIDEBAR (Scoreboard)
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
    
    if st.button("🔄 Reset Game (Keep Names)", use_container_width=True):
        st.session_state.p1_score = 0
        st.session_state.p2_score = 0
        st.session_state.current_player = 1
        st.session_state.current_card = None
        st.session_state.rounds_played = 0
        st.session_state.game_over = False
        st.rerun()

    if st.button("🧹 Master Reset (New Players)", use_container_width=True, type="primary"):
        st.session_state.clear()
        st.rerun()

# -----------------------------
# MAIN GAME PANEL
# -----------------------------
st.title(f"🔥 {PLAYERS[1]} vs {PLAYERS[2]}")
st.caption(f"Spicy Edition • First to {WIN_POINTS} points wins 🏆")

st.divider()

# WINNER DISPLAY
if st.session_state.game_over:
    winner = st.session_state.winner
    loser = PLAYERS[1] if winner == PLAYERS[2] else PLAYERS[2]
    
    st.success(f"🏆 **{winner} WINS THE GAME!**")
    st.error(f"💀 **{loser}, you must take a penalty shot or do a Double Dare!**")
    st.balloons()

# GAMEPLAY
elif st.session_state.current_card is None:
    # --- CARD SELECTION PHASE ---
    current_name = PLAYERS[st.session_state.current_player]
    st.subheader(f"🎲 {current_name}'s Turn")
    
    col1, col2 = st.columns(2)
    with col1:
        # Using callback to draw card
        st.button("😇 TRUTH", use_container_width=True, type="primary", 
                 on_click=draw_new_card, args=("Truth",))
    with col2:
        st.button("😈 DARE", use_container_width=True, type="secondary", 
                 on_click=draw_new_card, args=("Dare",))

else:
    # --- CARD REVEAL PHASE ---
    card = st.session_state.current_card
    
    if card['difficulty'] == 'Easy':
        color, emoji = "#4CAF50", "🌱"
    elif card['difficulty'] == 'Medium':
        color, emoji = "#FFA500", "🌶️"
    else:
        color, emoji = "#FF0000", "🔥"

    st.markdown(f"""
    <div style="padding: 20px; border: 2px solid {color}; border-radius: 10px; margin: 20px 0; background-color: #262730;">
        <h3 style="text-align: center; color: white;">{emoji} {card['difficulty'].upper()} {emoji}</h3>
        <h2 style="text-align: center; color: white;">{card['text']}</h2>
        <p style="text-align: center; color: #aaa;">Points: {card['points']}</p>
    </div>
    """, unsafe_allow_html=True)

    col_success, col_fail = st.columns(2)

    with col_success:
        # KEY FIX: Using on_click to ensure points add BEFORE screen refresh
        st.button("✅ Completed", use_container_width=True, 
                 on_click=handle_completion, args=(card['points'],))

    with col_fail:
        st.button("❌ Failed / Refused", use_container_width=True, 
                 on_click=handle_failure)
