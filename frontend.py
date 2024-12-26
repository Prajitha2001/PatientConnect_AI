import streamlit as st
from PIL import Image
import requests

def main():
    # Set page config
    st.set_page_config(page_title="HealthMate AI", page_icon="🩺", layout="wide")

    # App title and description
    st.title("🤖 HealthMate AI")
    st.subheader("Your Friendly AI for Mind and Body Care")
    st.write(
        "Ask me anything about your mental or physical health, and I'll guide you like a friendly doctor."
    )

    # Doctor Bot Image
    doctor_image = Image.open("doctor_bot.jpg")  # Replace with your bot image file
    st.image(doctor_image, caption="HealthMate AI", use_container_width=True)

    # Mind or Body Selector
    mode = st.sidebar.selectbox("Choose Your Focus:", ["Mental Problem", "Physical Problem"])

    # Conversation storage
    if "conversation" not in st.session_state:
        st.session_state["conversation"] = []

    # Input section based on mode
    if mode == "Mental Problem":
        st.header("🧠 Mental Health Support")
        user_query = st.text_input("What's on your mind?", placeholder="e.g., How do I manage stress?")
    else:
        st.header("🏋️ Physical Health Support")
        user_query = st.text_input("What's your physical health concern?", placeholder="e.g., How do I relieve back pain?")

    # Mode validation - check if the query is related to the wrong mode
    if user_query:
        physical_health_keywords = ["headache", "back", "stomach", "fatigue", "muscle", "joint","head", "eye", "ear", "mouth", "hand", "leg", "feet", "pain"]
        mental_health_keywords = ["stress", "anxiety", "depression", "mood", "mental", "fatigue", "sleep","mind"]

        # Check if query matches the selected mode
        if mode == "Mental Problem" and any(keyword in user_query.lower() for keyword in physical_health_keywords):
            st.warning("It seems like you're asking about a physical health issue. Please switch to 'Body' mode for physical health concerns.")
        elif mode == "Physical Problem" and any(keyword in user_query.lower() for keyword in mental_health_keywords):
            st.warning("It seems like you're asking about a mental health issue. Please switch to 'Mind' mode for mental health concerns.")
        else:
            # Submit button for correct mode
            if st.button("Ask HealthMate AI"):
                payload = {"query": user_query, "mode": mode}

                try:
                    # Simulating a backend request - Replace with your actual API endpoint
                    response = requests.post("http://127.0.0.1:5000/response", json=payload)
                    if response.status_code == 200:
                        data = response.json()
                        bot_response = data.get("response", "No response found.")

                        # Save conversation
                        st.session_state["conversation"].append(
                            {"mode": mode, "user": user_query, "bot": bot_response}
                        )
                    else:
                        st.error(f"Error {response.status_code}: Unable to get a response.")
                except requests.exceptions.RequestException as e:
                    st.error(f"An error occurred: {e}")

    # Display conversation history
    st.markdown("---")
    st.subheader("📜 Conversation History")
    for chat in st.session_state["conversation"]:
        if chat["mode"] == mode:  # Show only conversations related to the selected mode
            st.write(f"**You ({chat['mode']}):** {chat['user']}")
            st.write(f"**HealthMate AI:** {chat['bot']}")
            st.markdown("---")

if __name__ == "__main__":
    main()
