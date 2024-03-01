from flask import Flask, render_template, request
import cohere

app = Flask(__name__)
co = cohere.Client('D64OaZ9AtFWKEWrtaPTpKMFpaz5qfmLjrUESEyu0')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    message = request.form['message']
    response = co.chat(message, model="command", temperature=0.9)
    answer = response.text
    return answer

if __name__ == '__main__':
    app.run(debug=True)
    