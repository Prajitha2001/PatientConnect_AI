import streamlit as st
import requests

# Set up the Streamlit app
def main():
    # App title and configuration
    st.set_page_config(page_title="HealthSense AI", page_icon="💡")
    st.title("HealthSense AI 💡")
    st.markdown(
        """
        #### Welcome to HealthSense AI!  
        Your intelligent assistant for health and wellness queries.  
        Ask your questions and get tailored advice instantly.
        """
    )

    # Initialize session state for conversation history
    if "conversation" not in st.session_state:
        st.session_state["conversation"] = []

    # Chat display container
    st.markdown("### Chat History")
    chat_container = st.container()
    with chat_container:
        for chat in st.session_state["conversation"]:
            with st.chat_message("user"):
                st.markdown(f"{chat['user']}")
            with st.chat_message("assistant"):
                st.markdown(f"{chat['bot']}")

    # Chat input container
    st.markdown("### Talk to HealthSense AI")
    with st.form("chat_form", clear_on_submit=True):
        user_query = st.text_area(
            "Enter your message:",
            placeholder="Ask HealthSense AI anything about health and wellness...",
        )
        submit_button = st.form_submit_button("Send")

        if submit_button and user_query:
            # Prepare the payload for the POST request
            payload = {"query": user_query}

            try:
                # Make the POST request to the API endpoint
                response = requests.post("http://127.0.0.1:5000/response", json=payload)

                if response.status_code == 200:
                    # Parse the JSON response
                    data = response.json()

                    # Extract and display the chatbot response
                    bot_response = data.get("response", "No response found.")

                    # Append the conversation to session state
                    st.session_state["conversation"].append(
                        {"user": user_query, "bot": bot_response}
                    )
                    st.experimental_rerun()
                else:
                    st.error(
                        f"Error {response.status_code}: Unable to get a response from the API."
                    )
            except requests.exceptions.RequestException as e:
                st.error(f"An error occurred: {e}")
        elif submit_button:
            st.warning("Please enter a query before sending.")

    # Footer
    st.markdown(
        """
        ---
        *Powered by HealthSense AI. Your trusted health assistant.*  
        """
    )


if __name__ == "__main__":
    main()
