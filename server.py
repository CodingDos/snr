from flask import Flask, render_template, request, jsonify
import openai, os

app = Flask(__name__)

OPEN_API_KEY = os.getenv("API_KEY")

client = openai.Client(api_key=OPEN_API_KEY)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat-with-ai", methods=["POST"])
def chat():
    user_chat_msg = request.json.get("user_chat_msg")
    conversation = request.json.get("conversation")
    with open("./static/text/section599.md", "r") as file:
        guidlines = file.read()
    if len(conversation) == 0:
        conversation.append({
            "role": "system",
            "content": f"You are a compliance auditor professional in quality assurance for reviewing therapy sessions. Use this guidline to help with your answers to questions about cases, medical assistance, next steps, definitions, etc.:\n\n{guidlines}. Provide your answers as a string, no JSON, just text. Ensure to only answer questions related to the guidlines provided, if an irrelevant question appears please respond with unable to find an answer within the guidlines provided. Please provide section and subsection of any information found."
        })
    conversation.append({
        "role": "user",
        "content": user_chat_msg
    })

    ai_msg = send_convo_to_ai(conversation)
    print("ai_msg", ai_msg)

    conversation.append({
        "role": "assistant",
        "content": ai_msg
    })

    return jsonify({"ai_msg": ai_msg, 
                    "conversation": conversation})
    
def send_convo_to_ai(conversation):
    try:
        response = client.chat.completions.create(
            model = "gpt-4o",
            messages=conversation
        )
        return response.choices[0].message.content
    
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(debug=False)