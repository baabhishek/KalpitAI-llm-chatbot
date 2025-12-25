import streamlit as st
import openai


# ------------------------------------------------------------
# page setup
st.set_page_config(
    page_title="KalpitAI",
    page_icon="kalpit_logo.png",
    layout="centered"
)

# ------------------------------------------------------------
# css
st.markdown("""
<style>

html, body, .stApp {
    background-color: #ffffff;
    color: #111111;
}

.block-container {
    padding-top: 2.5rem;
    padding-bottom: 4rem;
}

/* Welcome text */
.welcome-title {
    text-align: center;
    font-size: 40px;
    font-weight: 600;
    margin-top: 80px;
    margin-bottom: 10px;
}

.welcome-sub {
    text-align: center;
    font-size: 18px;
    color: #555555;
    margin-bottom: 40px;
}

/* Chat message reset */
[data-testid="stChatMessage"] {
    background: transparent;
}

/* Assistant bubble */
[data-testid="stChatMessage"]:has(img[src*="Avatar_icon"])
.stChatMessageContent {
    background-color: #f7f7f8;
    padding: 14px 16px;
    border-radius: 12px;
}

/* User bubble */
[data-testid="stChatMessage"]:has(img[src*="user_icon"])
.stChatMessageContent {
    background-color: #eaeaea;
    padding: 14px 16px;
    border-radius: 12px;
}

/* Force readable text */
.stChatMessageContent *,
p, li, span, strong, em {
    color: #111111 !important;
    opacity: 1 !important;
}

/* Chat input */
[data-testid="stChatInput"] textarea {
    background-color: #f7f7f8;
    color: #111111;
    border-radius: 20px;
    border: 1px solid #cccccc;
}

/* Hide footer */
footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# api setup
#with open("key/openai_api_key.txt") as f:
#    api_key = f.read().strip()

#client = OpenAI()

# ------------------------------------------------------------
# HEADER (LOGO + NAME SAME LINE — STABLE)
st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 10], gap="small")

with col1:
    st.image("kalpit_logo.png", width=60)

with col2:
    st.markdown(
        "<h3 style='margin:6px 0 0 0;'>KalpitAI 1.0v</h3>",
        unsafe_allow_html=True
    )

# ------------------------------------------------------------
# SESSION STATE
if "messages" not in st.session_state:
    st.session_state.messages = []

# ------------------------------------------------------------
# CENTER WELCOME (FIRST LOAD ONLY)
if len(st.session_state.messages) == 0:
    st.markdown("<div class='welcome-title'>What can I help with?</div>", unsafe_allow_html=True)
    st.markdown("<div class='welcome-sub'>Hi, I’m Kalpit AI. Your everyday Al companion</div>", unsafe_allow_html=True)

# ------------------------------------------------------------
# CHAT HISTORY
for msg in st.session_state.messages:
    avatar = "Avatar_icon.png" if msg["role"] == "assistant" else "user_icon.png"
    st.chat_message(msg["role"], avatar=avatar).write(msg["content"])

# ------------------------------------------------------------
# CHAT INPUT
user_input = st.chat_input("Ask anything Type @ for mentioned")

if user_input:
    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Generate response
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content

    # Store assistant reply
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

    st.rerun()
