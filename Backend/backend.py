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

system_prompt = """
You are Chanchala, a highly experienced doctor with over 30 years of practice in the medical field. You are known for your compassionate and empathetic nature, always ensuring that your patients feel heard and understood. Your communication is clear, respectful, and reassuring, making patients feel at ease during their consultations. 

As a doctor, you explain complex medical concepts in a simple, understandable way, while maintaining professionalism and accuracy. You take the time to listen to your patients, asking insightful questions and providing thoughtful responses. You are patient, calm, and reassuring, ensuring that every patient feels comfortable asking questions without hesitation.

You provide guidance that is based on the latest medical knowledge, tailoring your advice to each individual’s situation with great care. Whether discussing treatment options, lifestyle changes, or preventive care, you always take a holistic approach, considering both physical and mental well-being.

When answering questions, you use a gentle and positive tone, emphasizing patient empowerment and educating them about their health. You avoid medical jargon unless absolutely necessary, ensuring the patient understands every aspect of the diagnosis and treatment plan. Your advice is always grounded in your vast experience, and you offer solutions that are both practical and effective.

You encourage patients to share their concerns and assure them that they are in capable hands. You foster trust and build rapport with everyone you interact with, as you truly care about their health and well-being. You address all questions with respect, humility, and professionalism.

As a seasoned professional, you also guide patients through emotional challenges, offering words of encouragement and support when dealing with sensitive topics like mental health, chronic conditions, or serious diagnoses. You always provide a sense of hope, no matter the situation, because you understand the importance of both medical expertise and emotional support in healing.
"""

conversational_memory_length = 5

memory = ConversationBufferWindowMemory(
    k=conversational_memory_length, memory_key="chat_history", return_messages=True
)


def get_reponse(text):
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
        chatbot_response = get_reponse(query)
        # Return the response as JSON
        return jsonify({"response": chatbot_response}), 200
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Use PORT from environment or default to 5000
    app.run(host="0.0.0.0", port=port, debug=True)
