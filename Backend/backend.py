import os
from dotenv import load_dotenv

from flask import Flask, request, jsonify
from flask_cors import CORS

from langchain.chains import LLMChain
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq

load_dotenv()

app = Flask(__name__)

CORS(app)

groq_api_key = os.environ.get("API_KEY")
model = "llama3-8b-8192"

client = ChatGroq(groq_api_key=groq_api_key, model_name=model)

# Common system prompt structure
def get_system_prompt(mode):
    if mode == "Mental Problem":
        specific_prompt = (
            "You are Chanchala, a patient seeking help for mental health concerns. Share your emotional state, stress levels, sleeping patterns, and any relevant personal challenges affecting your mental well-being. Be honest and open, as this helps the doctor provide accurate advice."
        )
    else:
        specific_prompt = (
            "You are Chanchala, a patient seeking help for physical health concerns. Describe your symptoms such as pain, discomfort, or other physical issues. Include relevant details about the onset, intensity, and any previous treatments attempted."
        )

    return (
        specific_prompt
        + "\n"
        "Maintain a tone that reflects your genuine concerns, using simple language. Be receptive to advice and provide enough details to assist the doctor in understanding your issue."
    )

# Conversation memory settings
conversational_memory_length = 5
memory = ConversationBufferWindowMemory(
    k=conversational_memory_length, memory_key="chat_history", return_messages=True
)

def get_response(text, mode):
    system_prompt = get_system_prompt(mode)
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content=system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{human_input}"),
        ]
    )
    conversation = LLMChain(
        llm=client,
        prompt=prompt,
        verbose=False,
        memory=memory,
    )
    response = conversation.predict(human_input=text)
    return response

@app.route("/response", methods=["POST"])
def response():
    try:
        data = request.get_json()
        query = data.get("query")
        mode = data.get("mode", "Mental Problem")  # Default to "Mental Problem" if not specified

        chatbot_response = get_response(query, mode)
        # Return the response as JSON
        return jsonify({"response": chatbot_response}), 200
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Use PORT from environment or default to 5000
    app.run(host="0.0.0.0", port=port, debug=True)
