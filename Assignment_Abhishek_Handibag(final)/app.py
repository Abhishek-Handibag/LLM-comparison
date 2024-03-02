#hblV44d7lwqno9sJPwiZhVuzv2ewkoDIbvGyBm6p
from flask import Flask, render_template, request
import cohere

app = Flask(__name__)
co = cohere.Client("hblV44d7lwqno9sJPwiZhVuzv2ewkoDIbvGyBm6p")  # Replace with your Cohere API key
gpt_api_key = "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"  # Replace with your ChatGPT API key

@app.route('/', methods=['GET', 'POST'])
def index():
    generated_cohere_text = None
    generated_chatgpt_text = None
    if request.method == 'POST':
        prompt = request.form['prompt']

        # Generate text using Cohere
        response_cohere = co.chat(prompt, model="command", temperature=0.9)
        generated_cohere_text = response_cohere.text

        # Generate text using ChatGPT
        response_chatgpt = generate_chatgpt_response(prompt)
        generated_chatgpt_text = response_chatgpt

    return render_template('index.html', generated_cohere_text=generated_cohere_text, generated_chatgpt_text=generated_chatgpt_text)

def generate_chatgpt_response(prompt):
    import requests
    import json

    # API endpoint for ChatGPT
    apiUrl = "https://api.openai.com/v1/chat/completions"

    data = {
        "model": "gpt-3.5-turbo-16k",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {gpt_api_key}"
    }

    try:
        response = requests.post(apiUrl, headers=headers, data=json.dumps(data))
        response_data = response.json()
        chatgpt_response = response_data["choices"][0]["message"]["content"]
        return chatgpt_response
    except Exception as e:
        print("Error:", e)
        return None

if __name__ == '__main__':
    app.run(debug=True)
