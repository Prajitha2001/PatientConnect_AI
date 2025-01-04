import streamlit as st
from PIL import Image
import requests

def main():
    # Set page config
    st.set_page_config(page_title="PatientConnect AI", page_icon="🩺", layout="wide")

    # App title and description
    col1, col2 = st.columns([3, 1])  # Use columns for layout
    with col1:
        st.title("🩺 PatientConnect AI")
        st.subheader("Your AI Companion for Health Concerns")
        st.write(
            "I am here to share my health concerns with you. Please guide me like the expert doctor you are."
        )
    with col2:
        doctor_image = Image.open("Patient_bot.png")  # Updated image filename
        resized_image = doctor_image.resize((200, 200))  # Resize the image
        st.image(resized_image, caption="PatientConnect AI")  # Display the resized image

    # Mind or Body Selector
    mode = st.sidebar.selectbox("Choose My Concern:", ["Mental Problem", "Physical Problem"])

    # Conversation storage
    if "conversation" not in st.session_state:
        st.session_state["conversation"] = []

    # Input section based on mode
    if mode == "Mental Problem":
        st.header("🧠 Mental Health Concern")
        user_query = st.text_input("What do you think about my concern?", placeholder="e.g., I often feel anxious.")
    else:
        st.header("🏋️ Physical Health Concern")
        user_query = st.text_input("Can you help with my physical issue?", placeholder="e.g., I have persistent back pain.")

    # Mode validation - check if the query is related to the wrong mode
    if user_query:
        physical_health_keywords = ["headache", "back", "stomach", "fatigue", "muscle", "joint", "head", "eye", "ear", "mouth", "hand", "leg", "feet", "pain"]
        mental_health_keywords = ["stress", "anxiety", "depression", "mood", "mental", "fatigue", "sleep", "mind"]

        # Check if query matches the selected mode
        if mode == "Mental Problem" and any(keyword in user_query.lower() for keyword in physical_health_keywords):
            st.warning("It seems like I mentioned a physical health issue. Please switch to 'Physical Problem' mode for such concerns.")
        elif mode == "Physical Problem" and any(keyword in user_query.lower() for keyword in mental_health_keywords):
            st.warning("It seems like I mentioned a mental health issue. Please switch to 'Mental Problem' mode for such concerns.")
        else:
            # Submit button for correct mode
            if st.button("Respond to My Concern"):
                payload = {"query": user_query, "mode": mode}

                try:
                    # Simulating a backend request - Replace with your actual API endpoint
                    response = requests.post("https://patientconnect-ai.onrender.com/response", json=payload)
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
            st.write(f"**Patient:** {chat['bot']}")
            st.markdown("---")

if __name__ == "__main__":
    main()
