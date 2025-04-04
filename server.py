from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import openai, os

app = Flask(__name__)

load_dotenv()

OPEN_API_KEY = os.getenv("API_KEY")

openai.api_key = OPEN_API_KEY

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat-with-ai", methods=["POST"])
def chat():
    user_chat_msg = request.json.get("user_chat_msg")
    md_file = request.json.get("md_file")
    conversation = request.json.get("conversation")
    md_file_path = os.path.join("./static/text/", md_file)
    with open(md_file_path, "r") as file:
        guidelines = file.read()
    if len(conversation) == 0:
        conversation.append({
            "role": "system",
            "content": f"""You are a compliance auditor professional in quality assurance for reviewing therapy sessions. Use this guideline to help with your answers to questions about cases, medical assistance, next steps, definitions, etc.:\n\n{guidelines}. 

            Provide your responses as a string, no JSON, just plain text. Ensure that all information incorporated from the guidelines is presented in quotes. After each quote, include a reference to the title and the specific section and subsection where the information was found in the format:

            <code><i> Reference: [Title], [Section Number], [Subsection Number] </i></code>

            Ensure your responses are structured as follows:
            1. If you find relevant information directly from the guidelines, quote it. Then decide if any words are important and wrap them in <b></b>.
            2. After quoting, on the next line follow with the reference in the format mentioned above.
            3. Any explanation, simplification, or advice in your own words should follow after the quote, not in quotes.
            5. If a question or request falls outside the scope of the guidelines, respond with: "Unable to find an answer within the guidelines provided."
            6. Please ensure all responses are clear, concise, and relevant to the information in the guidelines provided, and maintain proper structure in your responses."""
        })
    conversation.append({
        "role": "user",
        "content": user_chat_msg
    })

    ai_msg = send_convo_to_ai(conversation)
    print("ai_msg", ai_msg)
    
    ai_msg = ai_msg.replace("\n", "<br>")

    conversation.append({
        "role": "assistant",
        "content": ai_msg
    })

    return jsonify({"ai_msg": ai_msg, 
                    "conversation": conversation})
    
def send_convo_to_ai(conversation):
    try:
        response = openai.chat.completions.create(
            model = "gpt-4o",
            messages=conversation
        )
        return response.choices[0].message.content
    
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(debug=False)