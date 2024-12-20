import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.environ.get("API_KEY"),
)


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": """You are a Doctor also give some advice to regular check up on health.
            Provide response in consistent manner around 50 words.
            """,
        },
        {
            "role": "user",
            "content": "Having regular headahce",
        },
    ],
    model="llama3-8b-8192",
)

# print(chat_completion.choices[0].message.content)
print(chat_completion)


#  Generate Responses -> Create API (flask) -> UI (React / HTML+Css)