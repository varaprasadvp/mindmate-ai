import streamlit as st
import datetime

# Title
st.title("🧠 MindMate - AI Wellness Companion")

# Session state for storing chat and moods
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "moods" not in st.session_state:
    st.session_state["moods"] = []

# Chat Section
st.subheader("💬 Chat with MindMate")
user_input = st.text_input("How are you feeling today?")
if st.button("Send"):
    if user_input:
        # Simple response logic (replace with AI model later)
        if "stress" in user_input.lower():
            response = "I'm sorry to hear that. Let's try a 2-min breathing exercise together. 🌿"
        elif "sad" in user_input.lower():
            response = "It’s okay to feel sad sometimes. Remember, you’re not alone 💙"
        else:
            response = "Thanks for sharing. Remember to take care of yourself 💫"
        
        st.session_state["messages"].append(("You", user_input))
        st.session_state["messages"].append(("MindMate", response))

# Display Chat History
for sender, msg in st.session_state["messages"]:
    st.write(f"**{sender}:** {msg}")

# Mood Tracker
st.subheader("😊 Daily Mood Tracker")
mood = st.selectbox("Select your mood today:", ["Happy", "Okay", "Stressed", "Sad"])
if st.button("Log Mood"):
    st.session_state["moods"].append((datetime.date.today(), mood))
    st.success("Mood logged!")

# Mood History
if st.session_state["moods"]:
    st.subheader("📊 Mood History")
    for date, mood in st.session_state["moods"]:
        st.write(f"{date}: {mood}")
