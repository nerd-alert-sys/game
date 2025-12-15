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
    # Easy Truths (20)
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
    {"text": "What's your favorite food you'd never admit to eating?", "difficulty": "Easy", "points": 1},
    {"text": "Do you talk to yourself when no one is around?", "difficulty": "Easy", "points": 1},
    {"text": "What's the most childish thing you still enjoy?", "difficulty": "Easy", "points": 2},
    {"text": "Have you ever cried at a commercial?", "difficulty": "Easy", "points": 1},
    {"text": "What's your most unpopular opinion?", "difficulty": "Easy", "points": 2},
    {"text": "What's something you pretend to like but actually hate?", "difficulty": "Easy", "points": 2},
    
    # Medium Truths (30)
    {"text": "What is the most embarrassing thing you've done in public?", "difficulty": "Medium", "points": 4},
    {"text": "Have you ever practiced kissing on your hand?", "difficulty": "Medium", "points": 4},
    {"text": "What is the biggest lie you've ever told your parents?", "difficulty": "Medium", "points": 5},
    {"text": "Who in this room would you save first in a zombie apocalypse?", "difficulty": "Medium", "points": 5},
    {"text": "What is the meanest thing you've ever said to someone?", "difficulty": "Medium", "points": 5},
    {"text": "Have you ever picked your nose and ate it?", "difficulty": "Medium", "points": 6},
    {"text": "What is a secret you've kept from your best friend?", "difficulty": "Medium", "points": 6},
    {"text": "Have you ever peed in a pool?", "difficulty": "Medium", "points": 4},
    {"text": "What is the most trouble you've ever been in?", "difficulty": "Medium", "points": 5},
    {"text": "Have you ever sent a sext to the wrong person?", "difficulty": "Medium", "points": 6},
    {"text": "When was the last time you wet the bed?", "difficulty": "Medium", "points": 6},
    {"text": "What is the cringiest thing you posted on social media?", "difficulty": "Medium", "points": 4},
    {"text": "Have you ever lied to someone you love?", "difficulty": "Medium", "points": 5},
    {"text": "What's something you've done that you regret deeply?", "difficulty": "Medium", "points": 5},
    {"text": "Have you ever been jealous of a friend?", "difficulty": "Medium", "points": 4},
    {"text": "What's the worst advice you've ever given?", "difficulty": "Medium", "points": 4},
    {"text": "Have you ever copied someone's homework?", "difficulty": "Medium", "points": 4},
    {"text": "What's something you're secretly scared of?", "difficulty": "Medium", "points": 5},
    {"text": "Have you ever made fun of someone behind their back?", "difficulty": "Medium", "points": 5},
    {"text": "What's the furthest you've gone with someone you weren't dating?", "difficulty": "Medium", "points": 6},
    {"text": "Have you ever lied about your age to get into somewhere?", "difficulty": "Medium", "points": 4},
    {"text": "What's something you do that you think is weird?", "difficulty": "Medium", "points": 4},
    {"text": "Have you ever cried over a breakup?", "difficulty": "Medium", "points": 4},
    {"text": "What's the most money you've ever stolen?", "difficulty": "Medium", "points": 5},
    {"text": "Have you ever pretended to be sick to get out of something?", "difficulty": "Medium", "points": 4},
    {"text": "What's something you've never told anyone?", "difficulty": "Medium", "points": 6},
    {"text": "Have you ever hated someone in this room?", "difficulty": "Medium", "points": 5},
    {"text": "What's the worst thing you've done to a friend?", "difficulty": "Medium", "points": 5},
    {"text": "Have you ever been caught doing something embarrassing?", "difficulty": "Medium", "points": 4},
    {"text": "What's something you're addicted to?", "difficulty": "Medium", "points": 4},
    
    # Hard Truths (50)
    {"text": "What is your wildest fantasy?", "difficulty": "Hard", "points": 8},
    {"text": "Have you ever had a crush on a friend's partner?", "difficulty": "Hard", "points": 9},
    {"text": "What is the weirdest place you have ever done 'it'?", "difficulty": "Hard", "points": 10},
    {"text": "Rate the other player's looks on a scale of 1 to 10.", "difficulty": "Hard", "points": 8},
    {"text": "What is the most illegal thing you have ever done?", "difficulty": "Hard", "points": 9},
    {"text": "Who was your worst kiss and why?", "difficulty": "Hard", "points": 8},
    {"text": "Have you ever gone skinny dipping?", "difficulty": "Hard", "points": 7},
    {"text": "What is your favorite body part on the other player?", "difficulty": "Hard", "points": 9},
    {"text": "Have you ever flashed someone?", "difficulty": "Hard", "points": 9},
    {"text": "What is something you've done in bed that you'd never tell your parents?", "difficulty": "Hard", "points": 10},
    {"text": "If you had to sleep with one person from your work/school, who would it be?", "difficulty": "Hard", "points": 9},
    {"text": "What color is your underwear right now? Show proof.", "difficulty": "Hard", "points": 8},
    {"text": "Have you ever sent a nude photo?", "difficulty": "Hard", "points": 8},
    {"text": "Have you ever hooked up with a stranger?", "difficulty": "Hard", "points": 9},
    {"text": "What's something sexual you've thought about?", "difficulty": "Hard", "points": 8},
    {"text": "Have you ever been in love with someone you shouldn't have?", "difficulty": "Hard", "points": 9},
    {"text": "What's the kinkiest thing you've done?", "difficulty": "Hard", "points": 10},
    {"text": "Have you ever lied about sexual experience?", "difficulty": "Hard", "points": 8},
    {"text": "What's your biggest insecurity?", "difficulty": "Hard", "points": 9},
    {"text": "Have you ever cheated on someone?", "difficulty": "Hard", "points": 9},
    {"text": "What's the most selfish thing you've ever done?", "difficulty": "Hard", "points": 8},
    {"text": "Have you ever betrayed a friend's trust?", "difficulty": "Hard", "points": 9},
    {"text": "What's something you've done that you're deeply ashamed of?", "difficulty": "Hard", "points": 10},
    {"text": "Have you ever used someone for something?", "difficulty": "Hard", "points": 9},
    {"text": "What's a dark thought you've had?", "difficulty": "Hard", "points": 8},
    {"text": "Have you ever done something illegal with a friend?", "difficulty": "Hard", "points": 9},
    {"text": "What's the worst lie you've told a partner?", "difficulty": "Hard", "points": 10},
    {"text": "Have you ever watched something you shouldn't have?", "difficulty": "Hard", "points": 8},
    {"text": "What would you do for a large amount of money?", "difficulty": "Hard", "points": 9},
    {"text": "Have you ever fantasized about someone in this room?", "difficulty": "Hard", "points": 10},
    {"text": "What's something you do in private you'd never admit?", "difficulty": "Hard", "points": 9},
    {"text": "Have you ever considered being with the same gender?", "difficulty": "Hard", "points": 8},
    {"text": "What's the most violent thought you've had?", "difficulty": "Hard", "points": 9},
    {"text": "Have you ever stolen from someone you love?", "difficulty": "Hard", "points": 9},
    {"text": "What's something you've googled that embarrasses you?", "difficulty": "Hard", "points": 8},
    {"text": "Have you ever faked an orgasm?", "difficulty": "Hard", "points": 8},
    {"text": "What's your biggest turn-on?", "difficulty": "Hard", "points": 9},
    {"text": "Have you ever spied on someone?", "difficulty": "Hard", "points": 9},
    {"text": "What's the worst thing you've thought about someone here?", "difficulty": "Hard", "points": 10},
    {"text": "Have you ever wanted someone else's partner?", "difficulty": "Hard", "points": 9},
    {"text": "What's something you've done that could destroy your reputation?", "difficulty": "Hard", "points": 10},
    {"text": "Have you ever been attracted to someone you shouldn't be?", "difficulty": "Hard", "points": 8},
    {"text": "What's the worst rejection you've experienced?", "difficulty": "Hard", "points": 9},
    {"text": "Have you ever looked through someone's phone?", "difficulty": "Hard", "points": 9},
    {"text": "What's something you want but feel guilty for wanting?", "difficulty": "Hard", "points": 9},
    {"text": "Have you ever wished harm on someone?", "difficulty": "Hard", "points": 9},
    {"text": "What's the most painful secret you're keeping?", "difficulty": "Hard", "points": 10},
    {"text": "Have you ever done something you'd never want anyone to know?", "difficulty": "Hard", "points": 10},
]

DARES = [
    # Easy Dares (20)
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
    {"text": "Do a handstand against a wall.", "difficulty": "Easy", "points": 2},
    {"text": "Speak in a pirate accent for 2 minutes.", "difficulty": "Easy", "points": 2},
    {"text": "Do 15 jumping jacks.", "difficulty": "Easy", "points": 1},
    {"text": "Yodel as loud as you can.", "difficulty": "Easy", "points": 2},
    {"text": "Do a silly dance for 30 seconds.", "difficulty": "Easy", "points": 3},
    {"text": "Touch your toes for 10 seconds without bending your knees.", "difficulty": "Easy", "points": 1},
    
    # Medium Dares (30)
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
    {"text": "Recite the alphabet backwards.", "difficulty": "Medium", "points": 4},
    {"text": "Imitate the other player's walk for 1 minute.", "difficulty": "Medium", "points": 5},
    {"text": "Call someone and tell them a joke.", "difficulty": "Medium", "points": 5},
    {"text": "Do a runway walk across the room.", "difficulty": "Medium", "points": 4},
    {"text": "Eat something spicy and describe the flavor.", "difficulty": "Medium", "points": 5},
    {"text": "Let the other player take a selfie with you in a weird pose.", "difficulty": "Medium", "points": 4},
    {"text": "Whisper a secret into the other player's ear.", "difficulty": "Medium", "points": 5},
    {"text": "Do an impression of a celebrity.", "difficulty": "Medium", "points": 4},
    {"text": "Text your crush something nice (dictated by the other player).", "difficulty": "Medium", "points": 6},
    {"text": "Do a slow-motion walk for 1 minute.", "difficulty": "Medium", "points": 4},
    {"text": "Lick your elbow (attempt it).", "difficulty": "Medium", "points": 3},
    {"text": "Let the other player tie your shoes together.", "difficulty": "Medium", "points": 4},
    {"text": "Compliment the other player for 1 minute straight.", "difficulty": "Medium", "points": 5},
    {"text": "Do the worm on the floor.", "difficulty": "Medium", "points": 5},
    {"text": "Sniff the other player's armpit.", "difficulty": "Medium", "points": 4},
    {"text": "Do 20 burpees.", "difficulty": "Medium", "points": 4},
    {"text": "Let the other player put lipstick on you.", "difficulty": "Medium", "points": 5},
    {"text": "Sing a love song to the other player.", "difficulty": "Medium", "points": 5},
    
    # Hard Dares (50)
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
    {"text": "Kiss the other player on the lips for 10 seconds.", "difficulty": "Hard", "points": 10},
    {"text": "Let the other player control your phone for 1 minute.", "difficulty": "Hard", "points": 9},
    {"text": "Post a selfie in your underwear on your story (delete after 5 mins).", "difficulty": "Hard", "points": 10},
    {"text": "Tell the group your biggest secret.", "difficulty": "Hard", "points": 9},
    {"text": "Give the other player a body massage with oil.", "difficulty": "Hard", "points": 9},
    {"text": "Let the other player choose an embarrassing video for you to watch.", "difficulty": "Hard", "points": 8},
    {"text": "Flirt heavily with the other player for 2 minutes.", "difficulty": "Hard", "points": 9},
    {"text": "Take a suggestive photo with the other player.", "difficulty": "Hard", "points": 10},
    {"text": "Call someone and confess your feelings (or tell a made-up confession).", "difficulty": "Hard", "points": 9},
    {"text": "Do a handstand for 30 seconds.", "difficulty": "Hard", "points": 8},
    {"text": "Let the other player choose what you eat.", "difficulty": "Hard", "points": 7},
    {"text": "Dance seductively to a song of the other player's choice.", "difficulty": "Hard", "points": 9},
    {"text": "Let the other player wax a small part of your arm/leg.", "difficulty": "Hard", "points": 10},
    {"text": "Take a bath/shower with the other player (swimsuit only).", "difficulty": "Hard", "points": 10},
    {"text": "Let the other player dye a small streak of your hair.", "difficulty": "Hard", "points": 9},
    {"text": "Propose to the other player dramatically.", "difficulty": "Hard", "points": 8},
    {"text": "Let the other player take a video of you doing something embarrassing.", "difficulty": "Hard", "points": 9},
    {"text": "Kiss the other player passionately for 15 seconds.", "difficulty": "Hard", "points": 10},
    {"text": "Let the other player be your slave for the next round.", "difficulty": "Hard", "points": 9},
    {"text": "Do a photoshoot in lingerie (keep it tasteful).", "difficulty": "Hard", "points": 10},
    {"text": "Send a voice message saying something flirty to the other player.", "difficulty": "Hard", "points": 8},
    {"text": "Let the other player give you a lap dance.", "difficulty": "Hard", "points": 9},
    {"text": "Take off all your clothes except underwear for a photo.", "difficulty": "Hard", "points": 10},
    {"text": "Let the other player put makeup on you however they want.", "difficulty": "Hard", "points": 8},
    {"text": "Answer the next truth question completely honestly no matter what.", "difficulty": "Hard", "points": 9},
    {"text": "Let the other player control your outfit for the next 2 rounds.", "difficulty": "Hard", "points": 9},
    {"text": "Simulate a kiss with the other player (no lip contact).", "difficulty": "Hard", "points": 8},
    {"text": "Do 50 push-ups.", "difficulty": "Hard", "points": 7},
    {"text": "Let the other player blindfold you and touch you anywhere (clothed).", "difficulty": "Hard", "points": 9},
    {"text": "Create a TikTok dance with the other player.", "difficulty": "Hard", "points": 8},
    {"text": "Let the other player choose your hairstyle for the day.", "difficulty": "Hard", "points": 8},
    {"text": "Compliment the other player's body for 1 minute non-stop.", "difficulty": "Hard", "points": 9},
    {"text": "Let the other player take a suggestive photo of you.", "difficulty": "Hard", "points": 10},
    {"text": "Serenade the other player in your underwear.", "difficulty": "Hard", "points": 10},
    {"text": "Let the other player pierce your ear temporarily.", "difficulty": "Hard", "points": 8},
    {"text": "Write a romantic love letter to the other player.", "difficulty": "Hard", "points": 9},
]

# Verify we have 100 total
assert len(TRUTHS) == 50, f"Expected 50 truths, got {len(TRUTHS)}"
assert len(DARES) == 50, f"Expected 50 dares, got {len(DARES)}"

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
            weight = max(1, 5 - int(rounds/3))
        elif card["difficulty"] == "Medium":
            weight = 3 + int(rounds/4)
        else:
            weight = 1 + int(rounds/2)
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
    
    st.subheader("🔢 Round Counter")
    st.metric("Round", st.session_state.rounds_played)

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
    st.subheader(f"🎲 {current_name}'s Turn (Round {st.session_state.rounds_played + 1})")
    
    col1, col2 = st.columns(2)
    with col1:
        # Using callback to draw card
        st.button("😇 TRUTH", use_container_width=True, type="primary",
