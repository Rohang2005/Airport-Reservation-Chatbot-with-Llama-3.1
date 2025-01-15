from flask import Flask, render_template, request
from Airbot import download_flight_data, filter_flight_data, ask_llama

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']

    flight_data = download_flight_data()
    relevant_flights = filter_flight_data(flight_data, user_message)
    
    response = ask_llama(user_message, relevant_flights)

    return render_template('index.html', user_message=user_message, bot_response=response)

if __name__ == '__main__':
    app.run(debug=True)
