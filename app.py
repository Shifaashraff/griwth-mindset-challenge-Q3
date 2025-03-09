import streamlit as st
import random
from datetime import datetime

# Set page title and icon
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stHeader {
        color: #4CAF50;
    }
    .stProgress {
        background-color: #f0f0f0;
        border-radius: 10px;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Title and introduction
st.title("🌱 Growth Mindset Challenge")
st.write("""
Welcome to the Growth Mindset Challenge! This app is designed to help you adopt a growth mindset and track your progress.
""")

# What is a Growth Mindset?
st.header("What is a Growth Mindset?")
st.write("""
A growth mindset is the belief that your abilities and intelligence can be developed through hard work, perseverance, and learning from your mistakes. 
This concept was popularized by psychologist Carol Dweck, and it challenges the notion that our skills are fixed from the start. 
Instead, it reminds us that every challenge is an opportunity to learn and improve.
""")

# Why Adopt a Growth Mindset?
st.header("Why Adopt a Growth Mindset?")
st.write("""
- **Embrace Challenges**: View obstacles as opportunities to learn rather than as setbacks.
- **Learn from Mistakes**: Understand that making mistakes is a natural part of learning. Each error is a chance to improve.
- **Persist Through Difficulties**: Stay determined, even when things get tough. Hard work and persistence can lead to growth.
- **Celebrate Effort**: Recognize and reward the effort you put into learning, not just the final result.
- **Keep an Open Mind**: Stay curious and be willing to adapt your approach based on what you learn.
""")

# How to Practice a Growth Mindset
st.header("How to Practice a Growth Mindset")
st.write("""
- **Set Learning Goals**: Instead of only focusing on grades, set goals that help you develop new skills and understand complex concepts.
- **Reflect on Your Learning**: Regularly take time to think about what you’ve learned from both your successes and your challenges.
- **Seek Feedback**: Embrace constructive criticism and use it as a tool for improvement.
- **Stay Positive**: Believe in your capacity to grow, and encourage your peers to do the same.
""")

# Daily Growth Mindset Challenge
st.header("🌟 Daily Growth Mindset Challenge")
challenges = [
    "Reflect on a recent mistake and write down one thing you learned from it.",
    "Set a small learning goal for today and take the first step toward achieving it.",
    "Compliment someone on their effort rather than their talent.",
    "Try something new today, even if it feels uncomfortable.",
    "Write down three things you’re grateful for and how they contribute to your growth."
]

if "challenge" not in st.session_state:
    st.session_state.challenge = random.choice(challenges)

st.write("Today's Challenge:")
st.info(st.session_state.challenge)

if st.button("Get a New Challenge"):
    st.session_state.challenge = random.choice(challenges)
    st.experimental_rerun()

# Progress Tracker
st.header("📊 Progress Tracker")
if "progress" not in st.session_state:
    st.session_state.progress = 0

st.write("Track your progress by completing daily challenges:")
progress = st.slider("Progress", 0, 100, st.session_state.progress)
st.session_state.progress = progress

st.progress(progress)

# Inspirational Quotes or Videos
st.header("💡 Inspirational Quotes")
quotes = [
    "“The only limit to our realization of tomorrow is our doubts of today.” – Franklin D. Roosevelt",
    "“It’s not that I’m so smart, it’s just that I stay with problems longer.” – Albert Einstein",
    "“Success is no accident. It is hard work, perseverance, learning, studying, sacrifice, and most of all, love of what you are doing.” – Pelé",
    "“The only way to do great work is to love what you do.” – Steve Jobs",
    "“Believe you can and you’re halfway there.” – Theodore Roosevelt"
]

st.write("Here’s an inspirational quote for you:")
st.success(random.choice(quotes))

# Add a video
st.header("🎥 Inspirational Video")
st.write("Watch this short video to stay motivated:")
st.video("https://www.youtube.com/watch?v=H14bBuluwB8")  # Replace with your preferred video link

# Interactive Section: Growth Mindset Quiz
st.header("📝 Growth Mindset Quiz")
st.write("Take this short quiz to assess your current mindset:")

# Quiz Questions
q1 = st.radio("1. When faced with a difficult task, I tend to:", 
              ["Avoid it", "Give it a try but give up easily", "Persist and learn from the challenge"])
q2 = st.radio("2. I believe my intelligence and abilities are:", 
              ["Fixed and cannot change", "Somewhat changeable", "Can always improve with effort"])
q3 = st.radio("3. When I make a mistake, I:", 
              ["Feel discouraged", "Try to forget about it", "Learn from it and try again"])

# Quiz Scoring
if st.button("Submit Quiz"):
    score = 0
    if q1 == "Persist and learn from the challenge":
        score += 1
    if q2 == "Can always improve with effort":
        score += 1
    if q3 == "Learn from it and try again":
        score += 1

    st.write(f"Your score: {score}/3")
    if score == 3:
        st.success("You have a strong growth mindset! Keep it up!")
    elif score >= 1:
        st.warning("You have some growth mindset tendencies. Keep working on it!")
    else:
        st.error("You may have a fixed mindset. Consider adopting more growth mindset practices.")

# Footer
st.markdown("---")
st.write("Built with ❤️ using Streamlit")